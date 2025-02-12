=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_custom_templates</samp>](## "eos_designs_custom_templates") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- template</samp>](## "eos_designs_custom_templates.[].template") | String | Required |  |  | Template file. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;options</samp>](## "eos_designs_custom_templates.[].options") | Dictionary |  |  |  | Template options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list_merge</samp>](## "eos_designs_custom_templates.[].options.list_merge") | String |  | `append_rp` |  | Merge strategy for lists. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip_empty_keys</samp>](## "eos_designs_custom_templates.[].options.strip_empty_keys") | Boolean |  | `True` |  | Filter out keys from the generated output if value is null/none/undefined. |

=== "YAML"

    ```yaml
    eos_designs_custom_templates:
      - template: <str>
        options:
          list_merge: <str>
          strip_empty_keys: <bool>
    ```
