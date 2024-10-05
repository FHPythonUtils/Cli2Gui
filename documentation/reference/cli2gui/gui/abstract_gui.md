# AbstractGUI

[Cli2gui Index](../../README.md#cli2gui-index) / [Cli2gui](../index.md#cli2gui) / [Gui](./index.md#gui) / AbstractGUI

> Auto-generated documentation for [cli2gui.gui.abstract_gui](../../../../cli2gui/gui/abstract_gui.py) module.

- [AbstractGUI](#abstractgui)
  - [AbstractGUI](#abstractgui-1)
    - [AbstractGUI().main](#abstractgui()main)

## AbstractGUI

[Show source in abstract_gui.py:8](../../../../cli2gui/gui/abstract_gui.py#L8)

Abstract base class for GUI wrappers.

#### Signature

```python
class AbstractGUI(ABC):
    @abstractmethod
    def __init__(self) -> None: ...
```

### AbstractGUI().main

[Show source in abstract_gui.py:15](../../../../cli2gui/gui/abstract_gui.py#L15)

Abstract method for the main function.

#### Signature

```python
@abstractmethod
def main(
    self, buildSpec: types.FullBuildSpec, menu: list[str], quit_callback, run_callback
) -> None: ...
```