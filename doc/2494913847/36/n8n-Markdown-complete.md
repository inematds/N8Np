# n8n Knowledge Base

## Table of Contents

1. [n8n Project Overview](#n8n-project-overview)
2. [Core Concepts & Architecture](#core-concepts--architecture)
3. [n8n Workflow JSON Structure](#n8n-workflow-json-structure)
4. [JSON Generation Guidelines for AI](#json-generation-guidelines-for-ai)
5. [n8n Nodes](#n8n-nodes)
6. [Credentials Management](#credentials-management)
7. [Development & Contribution](#development--contribution)
8. [Complete Workflow Examples](#complete-workflow-examples)
9. [Summary](#summary)

---

## n8n Project Overview

### What is n8n?

n8n is a **workflow automation platform** that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.

### Key Capabilities

- **Code When You Need It**: Write JavaScript/Python, add npm packages, or use the visual interface
- **AI-Native Platform**: Build AI agent workflows based on LangChain with your own data and models
- **Full Control**: Self-host with our fair-code license or use the cloud offering
- **Enterprise-Ready**: Advanced permissions, SSO, and air-gapped deployments
- **Active Community**: 400+ integrations and 900+ ready-to-use templates

### What does n8n mean?

**Short answer:** It means "nodemation" and is pronounced as n-eight-n.

**Long answer:** The name comes from combining 'node-' (in the sense that it uses a Node-View and Node.js) and '-mation' for 'automation'. The shortened form 'n8n' was chosen for CLI convenience.

### Quick Start

Try n8n instantly with npx (requires Node.js):
```bash
npx n8n
```

Or deploy with Docker:
```bash
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Access the editor at http://localhost:5678

### License

n8n is fair-code distributed under:
- **Sustainable Use License** - for the core platform
- **n8n Enterprise License** - for additional enterprise features

Key points:
- **Source Available**: Always visible source code
- **Self-Hostable**: Deploy anywhere
- **Extensible**: Add your own nodes and functionality

### Resources

- [Documentation](https://docs.n8n.io)
- [400+ Integrations](https://n8n.io/integrations)
- [Example Workflows](https://n8n.io/workflows)
- [AI & LangChain Guide](https://docs.n8n.io/langchain/)
- [Community Forum](https://community.n8n.io)
- [Community Tutorials](https://community.n8n.io/c/tutorials/28)

### Directory Structure

The n8n mono-repository is organized as follows:

- `/docker/images` - Dockerfiles to create n8n containers
- `/packages` - The different n8n modules
  - `/packages/cli` - CLI code to run front- & backend
  - `/packages/core` - Core code handling workflow execution, webhooks, and workflows
  - `/packages/design-system` - Vue frontend components
  - `/packages/editor-ui` - Vue frontend workflow editor
  - `/packages/node-dev` - CLI to create new n8n-nodes
  - `/packages/nodes-base` - Base n8n nodes
  - `/packages/workflow` - Workflow code with interfaces used by front- & backend

---

## Core Concepts & Architecture

### Workflow Execution Model

n8n uses a node-based execution model where:
- **Nodes** are the building blocks that perform specific actions
- **Connections** define the flow of data between nodes
- **Executions** are instances of a workflow running with specific data

### Node Types

n8n supports several types of nodes:

1. **Trigger Nodes**: Start workflow execution
   - Manual Trigger
   - Webhook Trigger
   - Schedule Trigger (Cron)
   - Error Trigger
   - Workflow Trigger

2. **Action Nodes**: Perform operations
   - HTTP Request
   - Database operations
   - File operations
   - Data transformation

3. **AI Nodes**: AI/ML operations
   - LangChain integrations
   - OpenAI
   - AI Agents

### Connection Types

n8n supports multiple connection types:

```javascript
const NodeConnectionTypes = {
  AiAgent: 'ai_agent',
  AiChain: 'ai_chain',
  AiDocument: 'ai_document',
  AiEmbedding: 'ai_embedding',
  AiLanguageModel: 'ai_languageModel',
  AiMemory: 'ai_memory',
  AiOutputParser: 'ai_outputParser',
  AiRetriever: 'ai_retriever',
  AiTextSplitter: 'ai_textSplitter',
  AiTool: 'ai_tool',
  AiVectorStore: 'ai_vectorStore',
  Main: 'main',
};
```

### Execution Order

n8n supports different execution orders:
- **v0**: Legacy execution order
- **v1**: Improved execution order with better handling of multiple inputs

### Data Flow

1. **Input Data**: Each node receives data from connected nodes
2. **Processing**: Node executes its operation on the input data
3. **Output Data**: Processed data is passed to connected nodes
4. **Error Handling**: Errors can be caught and handled by error workflows

### Expression Language

n8n uses a JavaScript-based expression language for dynamic values:
- Wrapped in `{{ }}` syntax
- Access to workflow data, node outputs, and environment variables
- Example: `{{ $json.email }}` or `{{ $node['HTTP Request'].json.data }}`

### Workflow Metadata

Each workflow contains:
- **name**: Human-readable workflow name
- **nodes**: Array of node configurations
- **connections**: Object defining node connections
- **active**: Boolean indicating if workflow is active
- **settings**: Workflow-specific settings
- **versionId**: Unique version identifier
- **id**: Unique workflow identifier

---

## n8n Workflow JSON Structure

### Top-Level Structure

An n8n workflow is represented as a JSON object with the following top-level properties:

```json
{
  "name": "string",           // Workflow name
  "nodes": [],                // Array of node objects
  "connections": {},          // Object defining connections between nodes
  "active": boolean,          // Whether the workflow is active
  "settings": {},             // Workflow settings
  "versionId": "string",      // Version identifier
  "id": "string",             // Unique workflow ID
  "meta": {},                 // Metadata
  "tags": [],                 // Array of tags
  "pinData": {}              // Pinned data for testing
}
```

### Node Object Structure

Each node in the `nodes` array has this structure:

```json
{
  "parameters": {},           // Node-specific parameters
  "id": "string",            // Unique node ID
  "name": "string",          // Node instance name
  "type": "string",          // Node type (e.g., "n8n-nodes-base.httpRequest")
  "typeVersion": number,     // Version of the node type
  "position": [x, y],        // Visual position in editor
  "credentials": {           // Credentials used by the node
    "credentialType": {
      "id": "string",
      "name": "string"
    }
  },
  "disabled": boolean,       // Whether node is disabled (optional)
  "notes": "string",         // User notes (optional)
  "notesInFlow": boolean,    // Show notes in flow (optional)
  "retryOnFail": boolean,    // Retry on failure (optional)
  "maxTries": number,        // Max retry attempts (optional)
  "waitBetweenTries": number,// Wait time between retries (optional)
  "continueOnFail": boolean  // Continue workflow on failure (optional)
}
```

### Connections Structure

The `connections` object defines how nodes are connected:

```json
{
  "NodeName": {
    "main": [                // Main output
      [                      // First output
        {
          "node": "TargetNodeName",
          "type": "main",
          "index": 0         // Input index on target node
        }
      ]
    ],
    "ai_languageModel": [    // AI connection type example
      [
        {
          "node": "AI Agent",
          "type": "ai_languageModel",
          "index": 0
        }
      ]
    ]
  }
}
```

### Example: Simple HTTP Workflow

```json
{
  "name": "Simple HTTP Request Workflow",
  "nodes": [
    {
      "parameters": {},
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "name": "When clicking 'Execute workflow'",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "method": "GET",
        "url": "https://api.example.com/data",
        "options": {}
      },
      "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 3,
      "position": [450, 300]
    }
  ],
  "connections": {
    "When clicking 'Execute workflow'": {
      "main": [
        [
          {
            "node": "HTTP Request",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "c3d4e5f6-a7b8-9012-cdef-123456789012",
  "id": "d4e5f6a7-b8c9-0123-defa-234567890123",
  "meta": {
    "instanceId": "e5f6a7b8-c9d0-1234-efab-345678901234"
  },
  "tags": []
}
```

### Parameter Types

Node parameters can be of various types:

- **string**: Text input
- **number**: Numeric input
- **boolean**: True/false checkbox
- **options**: Dropdown selection
- **multiOptions**: Multiple selection
- **collection**: Group of related parameters
- **fixedCollection**: Collection with predefined structure
- **json**: JSON input
- **dateTime**: Date/time picker
- **color**: Color picker
- **hidden**: Hidden parameter
- **notice**: Informational notice
- **button**: Clickable button
- **resourceLocator**: Resource selector

---

## JSON Generation Guidelines for AI

### Essential Rules for Valid n8n Workflows

1. **Always include required top-level properties**:
   ```json
   {
     "name": "Workflow Name",
     "nodes": [],
     "connections": {},
     "active": false,
     "settings": {},
     "versionId": "generate-uuid-here",
     "id": "generate-uuid-here",
     "meta": {
       "instanceId": "generate-uuid-here"
     },
     "tags": []
   }
   ```

2. **Node IDs must be unique UUIDs** (format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

3. **Node positions must be arrays** with two numbers: `[x, y]`
   - Start around `[250, 300]` and increment by ~200-250 for each node

4. **Connection structure is nested arrays**:
   ```json
   "connections": {
     "Source Node Name": {
       "main": [
         [
           {
             "node": "Target Node Name",
             "type": "main",
             "index": 0
           }
         ]
       ]
     }
   }
   ```

### Common Workflow Patterns

#### 1. Linear Workflow (A → B → C)
```json
{
  "name": "Linear Workflow Example",
  "nodes": [
    {
      "parameters": {},
      "id": "uuid-1",
      "name": "Start",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "url": "https://api.example.com/data",
        "method": "GET"
      },
      "id": "uuid-2",
      "name": "HTTP Request",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 3,
      "position": [450, 300]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "processed",
              "value": "true"
            }
          ]
        }
      },
      "id": "uuid-3",
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [650, 300]
    }
  ],
  "connections": {
    "Start": {
      "main": [[{"node": "HTTP Request", "type": "main", "index": 0}]]
    },
    "HTTP Request": {
      "main": [[{"node": "Set", "type": "main", "index": 0}]]
    }
  },
  "active": false,
  "settings": {"executionOrder": "v1"},
  "versionId": "uuid-4",
  "id": "uuid-5",
  "meta": {"instanceId": "uuid-6"},
  "tags": []
}
```

#### 2. Branching Workflow (If/Else)
```json
{
  "connections": {
    "If": {
      "main": [
        [{"node": "True Branch", "type": "main", "index": 0}],
        [{"node": "False Branch", "type": "main", "index": 0}]
      ]
    }
  }
}
```

#### 3. Multiple Inputs (Merge)
```json
{
  "connections": {
    "Source 1": {
      "main": [[{"node": "Merge", "type": "main", "index": 0}]]
    },
    "Source 2": {
      "main": [[{"node": "Merge", "type": "main", "index": 1}]]
    }
  }
}
```

### Node Parameter Examples

#### HTTP Request with Authentication
```json
{
  "parameters": {
    "method": "POST",
    "url": "https://api.example.com/create",
    "authentication": "genericCredentialType",
    "genericAuthType": "httpHeaderAuth",
    "sendHeaders": true,
    "headerParameters": {
      "parameter": [
        {
          "name": "Content-Type",
          "value": "application/json"
        }
      ]
    },
    "sendBody": true,
    "bodyParameters": {
      "parameter": [
        {
          "name": "data",
          "value": "={{ $json }}"
        }
      ]
    }
  },
  "credentials": {
    "httpHeaderAuth": {
      "id": "credential-id",
      "name": "API Key Auth"
    }
  }
}
```

#### Schedule Trigger (Cron)
```json
{
  "parameters": {
    "triggerTimes": {
      "item": [
        {
          "mode": "everyX",
          "value": 5,
          "unit": "minutes"
        }
      ]
    }
  },
  "id": "uuid",
  "name": "Every 5 minutes",
  "type": "n8n-nodes-base.cron",
  "typeVersion": 1,
  "position": [250, 300]
}
```

#### Code Node with JavaScript
```json
{
  "parameters": {
    "language": "javaScript",
    "code": "// Access input data\nconst items = $input.all();\n\n// Process data\nconst processedItems = items.map(item => {\n  return {\n    json: {\n      ...item.json,\n      processed: true,\n      timestamp: new Date().toISOString()\n    }\n  };\n});\n\nreturn processedItems;"
  },
  "id": "uuid",
  "name": "Process Data",
  "type": "n8n-nodes-base.code",
  "typeVersion": 1,
  "position": [450, 300]
}
```

### Expression Syntax in Parameters

n8n uses expressions wrapped in `{{ }}` to access dynamic data:

- `{{ $json }}` - Current item's JSON data
- `{{ $json.fieldName }}` - Specific field from current item
- `{{ $node['Node Name'].json }}` - Data from a specific node
- `{{ $workflow.id }}` - Workflow metadata
- `{{ $env.VARIABLE_NAME }}` - Environment variables
- `{{ $now }}` - Current timestamp
- `{{ $today }}` - Today's date
- `{{ $items().length }}` - Number of items

### Common Mistakes to Avoid

1. **Missing required fields** - Every node needs `id`, `name`, `type`, `typeVersion`, `position`
2. **Invalid node types** - Use exact type strings like `n8n-nodes-base.httpRequest`
3. **Wrong connection structure** - Connections are always nested arrays
4. **Invalid expressions** - Expressions must be strings containing `{{ }}`
5. **Mismatched node names** - Connection node names must exactly match node `name` property

### Workflow Validation Checklist

- [ ] All nodes have unique IDs
- [ ] All nodes have positions as `[x, y]` arrays
- [ ] All referenced nodes in connections exist
- [ ] Node types are valid and include version
- [ ] Required parameters for each node type are included
- [ ] Expressions are properly formatted as strings
- [ ] Workflow has a name and ID
- [ ] Settings include `executionOrder: "v1"` for modern workflows

---

## Complete Workflow Examples

### Example 1: API Data Processing Workflow

This workflow fetches data from an API, processes it, and saves results.

```json
{
  "name": "API Data Processing",
  "nodes": [
    {
      "parameters": {},
      "id": "9b2e4b3f-1234-4567-8901-234567890123",
      "name": "When clicking \"Execute Workflow\"",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "url": "https://jsonplaceholder.typicode.com/users",
        "method": "GET",
        "options": {}
      },
      "id": "a1b2c3d4-5678-9012-3456-789012345678",
      "name": "Fetch Users",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 3,
      "position": [450, 300]
    },
    {
      "parameters": {
        "language": "javaScript",
        "code": "const users = $input.all();\n\nreturn users.map(item => {\n  const user = item.json;\n  return {\n    json: {\n      id: user.id,\n      fullName: user.name,\n      email: user.email,\n      company: user.company.name,\n      city: user.address.city\n    }\n  };\n});"
      },
      "id": "b2c3d4e5-6789-0123-4567-890123456789",
      "name": "Transform Data",
      "type": "n8n-nodes-base.code",
      "typeVersion": 1,
      "position": [650, 300]
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{ $json.city }}",
              "operation": "equals",
              "value2": "New York"
            }
          ]
        }
      },
      "id": "c3d4e5f6-7890-1234-5678-901234567890",
      "name": "Filter NY Users",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [850, 300]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "status",
              "value": "processed"
            },
            {
              "name": "timestamp",
              "value": "={{ new Date().toISOString() }}"
            }
          ]
        },
        "options": {}
      },
      "id": "d4e5f6a7-8901-2345-6789-012345678901",
      "name": "Add Metadata",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [1050, 250]
    }
  ],
  "connections": {
    "When clicking \"Execute Workflow\"": {
      "main": [
        [
          {
            "node": "Fetch Users",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Fetch Users": {
      "main": [
        [
          {
            "node": "Transform Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Transform Data": {
      "main": [
        [
          {
            "node": "Filter NY Users",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Filter NY Users": {
      "main": [
        [
          {
            "node": "Add Metadata",
            "type": "main",
            "index": 0
          }
        ],
        []
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "e5f6a7b8-9012-3456-7890-123456789012",
  "id": "f6a7b8c9-0123-4567-8901-234567890123",
  "meta": {
    "instanceId": "a7b8c9d0-1234-5678-9012-345678901234"
  },
  "tags": []
}
```

### Example 2: Scheduled Database Sync

This workflow runs every hour to sync data between systems.

```json
{
  "name": "Hourly Database Sync",
  "nodes": [
    {
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "mode": "everyX",
              "value": 1,
              "unit": "hours"
            }
          ]
        }
      },
      "id": "11111111-2222-3333-4444-555555555555",
      "name": "Every Hour",
      "type": "n8n-nodes-base.cron",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "operation": "executeQuery",
        "query": "SELECT * FROM users WHERE updated_at > NOW() - INTERVAL 1 HOUR"
      },
      "id": "22222222-3333-4444-5555-666666666666",
      "name": "Get Updated Users",
      "type": "n8n-nodes-base.postgres",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "postgres": {
          "id": "cred-id-1",
          "name": "Postgres DB"
        }
      }
    },
    {
      "parameters": {
        "mode": "append",
        "mergeByFields": {
          "values": [
            {
              "field1": "id",
              "field2": "id"
            }
          ]
        }
      },
      "id": "33333333-4444-5555-6666-777777777777",
      "name": "Merge",
      "type": "n8n-nodes-base.merge",
      "typeVersion": 2,
      "position": [650, 300]
    },
    {
      "parameters": {
        "url": "={{ $env.API_ENDPOINT }}/users/{{ $json.id }}",
        "method": "PUT",
        "sendBody": true,
        "bodyParameters": {
          "parameter": [
            {
              "name": "",
              "value": "={{ $json }}"
            }
          ]
        },
        "options": {
          "batching": {
            "batch": {
              "batchSize": 10,
              "batchInterval": 1000
            }
          }
        }
      },
      "id": "44444444-5555-6666-7777-888888888888",
      "name": "Update API",
      "type": "n8n-nodes-base.httpRequest",
      "typeVersion": 3,
      "position": [850, 300]
    }
  ],
  "connections": {
    "Every Hour": {
      "main": [
        [
          {
            "node": "Get Updated Users",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Get Updated Users": {
      "main": [
        [
          {
            "node": "Merge",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Merge": {
      "main": [
        [
          {
            "node": "Update API",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {
    "executionOrder": "v1",
    "errorWorkflow": "error-handler-workflow-id"
  },
  "versionId": "55555555-6666-7777-8888-999999999999",
  "id": "66666666-7777-8888-9999-000000000000",
  "meta": {
    "instanceId": "77777777-8888-9999-0000-111111111111"
  },
  "tags": ["sync", "database", "scheduled"]
}
```

### Example 3: Webhook with Error Handling

This workflow receives webhooks and includes error handling.

```json
{
  "name": "Webhook Processing with Error Handling",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "process-order",
        "responseMode": "responseNode",
        "options": {
          "rawBody": true
        }
      },
      "id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "language": "javaScript",
        "code": "const body = JSON.parse($input.first().json.body);\n\nif (!body.orderId || !body.amount) {\n  throw new Error('Missing required fields');\n}\n\nreturn [{\n  json: {\n    orderId: body.orderId,\n    amount: body.amount,\n    processedAt: new Date().toISOString()\n  }\n}];"
      },
      "id": "bbbbbbbb-cccc-dddd-eeee-ffffffffffff",
      "name": "Validate & Process",
      "type": "n8n-nodes-base.code",
      "typeVersion": 1,
      "position": [450, 300],
      "continueOnFail": true
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{ $node[\"Validate & Process\"].error ? true : false }}",
              "value2": true
            }
          ]
        }
      },
      "id": "cccccccc-dddd-eeee-ffff-000000000000",
      "name": "Check Error",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [650, 300]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "status",
              "value": "error"
            },
            {
              "name": "message",
              "value": "={{ $node[\"Validate & Process\"].error.message }}"
            }
          ]
        }
      },
      "id": "dddddddd-eeee-ffff-0000-111111111111",
      "name": "Error Response",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [850, 200]
    },
    {
      "parameters": {
        "values": {
          "string": [
            {
              "name": "status",
              "value": "success"
            }
          ]
        }
      },
      "id": "eeeeeeee-ffff-0000-1111-222222222222",
      "name": "Success Response",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [850, 400]
    },
    {
      "parameters": {
        "options": {}
      },
      "id": "ffffffff-0000-1111-2222-333333333333",
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [1050, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "Validate & Process",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Validate & Process": {
      "main": [
        [
          {
            "node": "Check Error",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Check Error": {
      "main": [
        [
          {
            "node": "Error Response",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Success Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Error Response": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Success Response": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1"
  },
  "versionId": "00000000-1111-2222-3333-444444444444",
  "id": "11111111-2222-3333-4444-555555555555",
  "meta": {
    "instanceId": "22222222-3333-4444-5555-666666666666"
  },
  "tags": ["webhook", "api", "error-handling"]
}
```

---

## n8n Nodes

### Overview

n8n provides 400+ built-in nodes organized in categories. Each node has:
- **Display Name**: User-friendly name shown in UI
- **Internal Name/Type**: Programmatic identifier
- **Version**: Node definition version
- **Parameters**: Configurable options
- **Inputs/Outputs**: Connection points
- **Credentials**: Authentication requirements

### Core Trigger Nodes

#### Manual Trigger

- **Type**: `n8n-nodes-base.manualTrigger`
- **Display Name**: Manual Trigger
- **Description**: Runs the flow on clicking a button in n8n
- **Icon**: `fa:mouse-pointer`
- **Group**: `['trigger']`
- **Version**: 1
- **Inputs**: None
- **Outputs**: `['main']`
- **Parameters**:
  - `notice` (type: notice): Informational message about workflow execution

#### Webhook Trigger

- **Type**: `n8n-nodes-base.webhook`
- **Display Name**: Webhook
- **Description**: Starts workflow on webhook call
- **Parameters**:
  - `httpMethod`: HTTP method to listen for (GET, POST, etc.)
  - `path`: Webhook path
  - `responseMode`: How to respond (immediately, at end of workflow, etc.)
  - `options`: Additional options (binary data, raw body, etc.)

#### Schedule Trigger (Cron)

- **Type**: `n8n-nodes-base.cron`
- **Display Name**: Schedule Trigger
- **Description**: Triggers workflow on a schedule
- **Parameters**:
  - `triggerTimes`: Cron expression or interval settings

### Core Action Nodes

#### HTTP Request

- **Type**: `n8n-nodes-base.httpRequest`
- **Display Name**: HTTP Request
- **Description**: Makes HTTP requests to external services
- **Version**: 3, 4, 4.1, 4.2
- **Icon**: Color `#0004F5`
- **Subtitle**: `={{$parameter["method"] + ": " + $parameter["url"]}}`
- **Parameters**:
  - `method` (options): HTTP method (GET, POST, PUT, DELETE, etc.)
  - `url` (string): URL to make request to
  - `authentication` (options): Authentication type
  - `sendQuery` (boolean): Whether to send query parameters
  - `queryParameters` (fixedCollection): Query parameters
  - `sendHeaders` (boolean): Whether to send headers
  - `headerParameters` (fixedCollection): Header parameters
  - `sendBody` (boolean): Whether to send body
  - `bodyParameters` (fixedCollection): Body parameters
  - `options` (collection): Additional options (timeout, proxy, pagination, etc.)

#### Set

- **Type**: `n8n-nodes-base.set`
- **Display Name**: Set
- **Description**: Sets values on items
- **Parameters**:
  - `values` (fixedCollection): Values to set
  - `options`: Keep only set values, dot notation, etc.

#### If

- **Type**: `n8n-nodes-base.if`
- **Display Name**: If
- **Description**: Conditional branching
- **Outputs**: `['main', 'main']` (true/false branches)
- **Parameters**:
  - `conditions` (fixedCollection): Conditions to evaluate

#### Code

- **Type**: `n8n-nodes-base.code`
- **Display Name**: Code
- **Description**: Execute custom JavaScript code
- **Parameters**:
  - `language`: Programming language (JavaScript/Python)
  - `code`: Code to execute

### Data Transformation Nodes

#### Merge

- **Type**: `n8n-nodes-base.merge`
- **Display Name**: Merge
- **Description**: Merges data from multiple inputs
- **Parameters**:
  - `mode`: Merge mode (append, merge by key, etc.)

#### Split In Batches

- **Type**: `n8n-nodes-base.splitInBatches`
- **Display Name**: Split In Batches
- **Description**: Splits data into smaller batches
- **Parameters**:
  - `batchSize`: Size of each batch
  - `options`: Reset, pause between batches

#### Item Lists

- **Type**: `n8n-nodes-base.itemLists`
- **Display Name**: Item Lists
- **Description**: Perform operations on lists
- **Parameters**:
  - `operation`: Operation type (aggregate, sort, limit, etc.)

### Database Nodes

#### MySQL

- **Type**: `n8n-nodes-base.mySql`
- **Display Name**: MySQL
- **Description**: Interact with MySQL databases
- **Credentials**: MySQL credentials required
- **Parameters**:
  - `operation`: Operation type (execute query, insert, update, delete)
  - `query`: SQL query (for execute query)
  - `table`: Table name
  - `columns`: Columns for insert/update

#### PostgreSQL

- **Type**: `n8n-nodes-base.postgres`
- **Display Name**: Postgres
- **Description**: Interact with PostgreSQL databases
- **Similar structure to MySQL**

#### MongoDB

- **Type**: `n8n-nodes-base.mongoDb`
- **Display Name**: MongoDB
- **Description**: Interact with MongoDB databases
- **Parameters**:
  - `operation`: Operation type (find, insert, update, delete)
  - `collection`: Collection name
  - `query`: MongoDB query

### File System Nodes

#### Read Binary Files

- **Type**: `n8n-nodes-base.readBinaryFiles`
- **Display Name**: Read Binary Files
- **Description**: Reads binary files from disk
- **Parameters**:
  - `filePath`: Path to file
  - `property`: Property name to store binary data

#### Write Binary File

- **Type**: `n8n-nodes-base.writeBinaryFile`
- **Display Name**: Write Binary File
- **Description**: Writes binary files to disk
- **Parameters**:
  - `fileName`: Output file name
  - `property`: Property containing binary data

### AI/LangChain Nodes

#### OpenAI Chat Model

- **Type**: `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- **Display Name**: OpenAI Chat Model
- **Description**: OpenAI language model for chat
- **Credentials**: OpenAI API credentials required
- **Connection Type**: `ai_languageModel`

#### AI Agent

- **Type**: `@n8n/n8n-nodes-langchain.agent`
- **Display Name**: AI Agent
- **Description**: AI agent that can use tools and memory
- **Inputs**: `['main', 'ai_languageModel', 'ai_memory', 'ai_tool']`
- **Parameters**:
  - `text`: Input text/prompt
  - `options`: Additional agent options

---

## Credentials Management

### Overview

n8n provides a secure credential management system that:
- Stores credentials encrypted in the database
- Allows sharing credentials across workflows
- Supports OAuth2, API keys, and custom authentication
- Provides credential testing functionality

### Credential Structure

```json
{
  "id": "string",
  "name": "string",
  "type": "string",
  "data": {}, // Encrypted credential data
  "nodesAccess": [
    {
      "nodeType": "string",
      "date": "ISO 8601 date"
    }
  ]
}
```

### Common Credential Types

#### API Key Authentication
- **Type**: Various (service-specific)
- **Fields**: Usually `apiKey`, sometimes `domain` or `subdomain`
- **Example**: OpenAI, SendGrid, Stripe

#### OAuth2
- **Type**: `OAuth2Api`
- **Fields**: `clientId`, `clientSecret`, `accessTokenUrl`, `authUrl`
- **Flow**: Authorization Code, Client Credentials

#### Basic Authentication
- **Type**: Various (often embedded in nodes)
- **Fields**: `username`, `password`
- **Example**: HTTP Request node basic auth

#### Database Credentials
- **MySQL**: `host`, `port`, `database`, `user`, `password`
- **PostgreSQL**: Similar to MySQL
- **MongoDB**: `connectionString` or individual fields

### Using Credentials in Workflows

1. **Node Level**: Credentials are selected in node configuration
2. **Workflow Level**: Credentials can be shared across nodes
3. **Testing**: Built-in test functionality for most credential types

### Security Best Practices

- Store sensitive data only in credential fields
- Never hardcode credentials in node parameters
- Use environment variables for deployment-specific values
- Regularly rotate credentials
- Limit credential access to necessary nodes

---

## Development & Contribution

### Development Setup

1. **Requirements**:
   - Node.js >= 18.17
   - pnpm >= 9.1
   - Git

2. **Initial Setup**:
   ```bash
   git clone https://github.com/n8n-io/n8n.git
   cd n8n
   pnpm install
   pnpm build
   ```

3. **Start Development**:
   ```bash
   pnpm dev
   ```

### Creating Custom Nodes

1. **Use n8n-node-dev CLI**:
   ```bash
   npx n8n-node-dev new
   ```

2. **Node Structure**:
   ```typescript
   import { INodeType, INodeTypeDescription } from 'n8n-workflow';

   export class MyNode implements INodeType {
     description: INodeTypeDescription = {
       displayName: 'My Node',
       name: 'myNode',
       group: ['transform'],
       version: 1,
       description: 'My custom node',
       defaults: {
         name: 'My Node',
       },
       inputs: ['main'],
       outputs: ['main'],
       properties: [
         // Node properties
       ],
     };

     async execute(this: IExecuteFunctions) {
       // Node logic
     }
   }
   ```

3. **Testing Nodes**:
   - Use the n8n UI for manual testing
   - Write unit tests for complex logic
   - Test error handling and edge cases

### Contribution Guidelines

1. **Code Style**:
   - Follow existing code patterns
   - Use TypeScript
   - Run `pnpm format` before committing

2. **Pull Request Process**:
   - Fork the repository
   - Create feature branch from `master`
   - Make changes and test thoroughly
   - Submit PR with clear description
   - Sign the CLA

3. **Commit Messages**:
   - Use conventional commits format
   - Examples:
     - `feat(editor): Add new feature`
     - `fix(core): Fix bug in execution`
     - `docs: Update README`

4. **Testing**:
   - Add tests for new functionality
   - Ensure existing tests pass
   - Test manually in the UI

### Community Resources

- **Forum**: https://community.n8n.io
- **Discord**: Community chat
- **GitHub Issues**: Bug reports and feature requests
- **Documentation**: https://docs.n8n.io

### Development Tips

1. **Debugging**:
   - Use VS Code debugger
   - Add console.logs in development
   - Check browser console for frontend issues

2. **Performance**:
   - Handle large datasets efficiently
   - Use streaming where possible
   - Implement pagination for API calls

3. **Error Handling**:
   - Provide clear error messages
   - Use try-catch blocks
   - Allow workflows to continue on error when appropriate

---

## Summary

This knowledge base provides a comprehensive overview of n8n's architecture, workflow structure, and node system. Key takeaways:

1. **n8n is a powerful workflow automation platform** with 400+ integrations and AI capabilities
2. **Workflows are JSON-based** with nodes, connections, and settings
3. **Nodes are the building blocks** with specific types, parameters, and connection points
4. **Credentials are managed securely** with encryption and access controls
5. **Development is straightforward** with clear guidelines and community support

Use this knowledge base to:
- Understand n8n's structure and capabilities
- Create and modify workflows programmatically
- Develop custom nodes and integrations
- Contribute to the n8n project

For the latest information and updates, always refer to the official n8n documentation at https://docs.n8n.io.
