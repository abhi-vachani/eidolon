// This file is auto-generated by @hey-api/openapi-ts


export const $HTTPValidationError = {
    properties: {
        detail: {
            items: {
                '$ref': '#/components/schemas/ValidationError'
            },
            type: 'array',
            title: 'Detail'
        }
    },
    type: 'object',
    title: 'HTTPValidationError'
} as const;

export const $UsageDelta = {
    properties: {
        type: {
            type: 'string',
            enum: ['delta'],
            const: 'delta',
            title: 'Type',
            default: 'delta'
        },
        used_delta: {
            type: 'integer',
            title: 'Used Delta',
            default: 0
        },
        allowed_delta: {
            type: 'integer',
            title: 'Allowed Delta',
            default: 0
        },
        extra: {
            type: 'object',
            title: 'Extra',
            default: {}
        }
    },
    type: 'object',
    title: 'UsageDelta'
} as const;

export const $UsageReset = {
    properties: {
        type: {
            type: 'string',
            enum: ['reset'],
            const: 'reset',
            title: 'Type',
            default: 'reset'
        },
        used: {
            type: 'integer',
            title: 'Used',
            default: 0
        },
        allowed: {
            type: 'integer',
            title: 'Allowed',
            default: 600
        },
        extra: {
            type: 'object',
            title: 'Extra',
            default: {}
        }
    },
    type: 'object',
    title: 'UsageReset'
} as const;

export const $UsageSummary = {
    properties: {
        subject: {
            type: 'string',
            title: 'Subject'
        },
        used: {
            type: 'integer',
            title: 'Used'
        },
        allowed: {
            type: 'integer',
            title: 'Allowed'
        }
    },
    type: 'object',
    required: ['subject', 'used', 'allowed'],
    title: 'UsageSummary'
} as const;

export const $ValidationError = {
    properties: {
        loc: {
            items: {
                anyOf: [
                    {
                        type: 'string'
                    },
                    {
                        type: 'integer'
                    }
                ]
            },
            type: 'array',
            title: 'Location'
        },
        msg: {
            type: 'string',
            title: 'Message'
        },
        type: {
            type: 'string',
            title: 'Error Type'
        }
    },
    type: 'object',
    required: ['loc', 'msg', 'type'],
    title: 'ValidationError'
} as const;