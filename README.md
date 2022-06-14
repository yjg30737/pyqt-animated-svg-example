# pyqt_animated_svg_example
PyQt animated SVG example

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install git+https://github.com/yjg30737/pyqt-animated-svg-example.git --upgrade`

## Example
```python
import sys

from PyQt5.QtWidgets import QApplication
from pyqt_animated_svg_example import AnimatedSvgExample


if __name__ == "__main__":
    app = QApplication(sys.argv)
    r = AnimatedSvgExample()
    r.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/173474471-3e181644-b68a-4929-85f0-3ceea955e72d.mp4

Note: I will use this to something useful later.
