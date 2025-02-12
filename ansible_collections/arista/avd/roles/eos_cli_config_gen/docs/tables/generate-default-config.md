=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>generate_default_config</samp>](## "generate_default_config") | Boolean |  | `True` |  | The `generate_default_config` knob allows to omit default EOS configuration.<br>This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.<br><br>The following commands will be omitted when `generate_default_config` is set to `false`:<br><br>- RANCID Content Type<br>- Hostname<br>- Default configuration for `aaa`<br>- Default configuration for `enable password`<br>- Transceiver qsfp default mode<br>- End of configuration delimiter |

=== "YAML"

    ```yaml
    generate_default_config: <bool>
    ```
