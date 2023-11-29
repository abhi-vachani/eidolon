import hashlib
import json
from typing import List

from pydantic import Field
from pydantic import ValidationError

from eidolon_sdk.cpu.call_context import CallContext
from eidolon_sdk.cpu.llm_message import LLMMessage, AssistantMessage
from eidolon_sdk.cpu.llm_unit import LLMUnit, LLMUnitConfig, LLMCallFunction
from eidolon_sdk.impl.llm.open_ai_llm_unit import OpenAiGPTSpec
from eidolon_sdk.reference_model import Specable, Reference
from eidolon_sdk.util.class_utils import fqn


# Assuming CallContext, LLMMessage, LLMCallFunction, AssistantMessage are defined elsewhere

class CacheLLMSpec(LLMUnitConfig):
    dir: str = Field(default="llm_cache", description="The directory to store the cache in.")
    llm: Reference[LLMUnit] = Field(default=Reference(implementation=fqn(OpenAiGPTSpec)), description="The LLM to cache.")


class CacheLLM(LLMUnit, Specable[CacheLLMSpec]):
    dir: str

    def __init__(self, spec: CacheLLMSpec, **kwargs):
        super().__init__(spec, **kwargs)
        self.dir = spec.dir
        self.llm = spec.llm.instantiate(agent_memory=self.agent_memory, processing_unit_locator=self.processing_unit_locator)

    async def execute_llm(self, call_context: CallContext, inMessages: List[LLMMessage], inTools: List[LLMCallFunction], output_format: dict) -> AssistantMessage:
        try:
            # Ensure inputs are valid
            validated_messages = [LLMMessage(**message.model_dump()) for message in inMessages]
            validated_tools = [LLMCallFunction(**tool.model_dump()) for tool in inTools]

            # Generate the hash
            combined_str = ''.join(message.model_dump_json() for message in validated_messages) + \
                           ''.join(tool.model_dump_json() for tool in validated_tools) + \
                           json.dumps(output_format)

            hash_object = hashlib.sha256()
            hash_object.update(combined_str.encode())
            hash_hex = hash_object.hexdigest()

            file_name = f"{self.dir}/{hash_hex}.json"

            if self.agent_memory.file_memory.exists(file_name):
                contents = self.agent_memory.file_memory.read_file(file_name)
                return AssistantMessage.model_validate(**json.loads(contents.decode()))
            else:
                result = await self.llm.execute_llm(call_context, validated_messages, validated_tools, output_format)
                self.agent_memory.file_memory.write_file(file_name, json.dumps(result.dict()).encode())
                return result
        except ValidationError as ve:
            # Handle Pydantic validation errors
            raise ValueError(f"Input validation error: {ve}")
        except json.JSONDecodeError:
            # Handle JSON errors
            raise ValueError("Error in JSON processing")
        except IOError as io_err:
            # Handle File IO errors
            raise IOError(f"File operation error: {io_err}")
        except Exception as e:
            # Handle other exceptions
            raise Exception(f"Unexpected error occurred: {e}")

