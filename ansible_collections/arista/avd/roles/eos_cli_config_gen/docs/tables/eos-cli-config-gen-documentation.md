=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_cli_config_gen_documentation</samp>](## "eos_cli_config_gen_documentation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_documentation.hide_passwords") | Boolean |  | `True` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true<br> |

=== "YAML"

    ```yaml
    eos_cli_config_gen_documentation:
      hide_passwords: <bool>
    ```
