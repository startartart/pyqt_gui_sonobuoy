# pyqt_sonobuoy_gui
### ⓒ PyDracula - Modern GUI PySide6 / PyQt6
---
> **Warning**: 이 프로젝트는 PySide6 및 Python 3.9를 사용하여 생성되었으며 이전 버전을 사용하면 호환성 문제가 발생할 수 있습니다.

# Running
> 다음 시스템의 필수 라이브러리를 설치해주세요. 
시스템에 따라 아래 명령을 실행합니다. 
```
pip install PySide6
python main.py
```

# Project Files And Folders
> **main.py**: 응용 프로그램 초기화 파일

> **main.ui**: Qt 디자이너 프로젝트

> **resouces.qrc**: Qt Designer 자원 사용자는 Qt Designer를 사용하여 여기에 자원을 추가하십시오. 버전 6 사용

> **setup.py**: 애플리케이션을 컴파일하기 위한 cx-Freeze 설정(Windows용으로 구성됨).

> **themes/**: 여기에 테마(.qss)를 추가합니다.

> **modules/**: GUI를 실행하기 위한 모듈입니다.

> **modules/app_funtions.py**: 여기에 애플리케이션의 기능을 추가하십시오.

> **modules/app_settings.py**: 사용자 인터페이스를 구성하는 전역 변수.

> **modules/resources_rc.py**: 다음 명령을 사용하여 "resources.qrc를 컴파일합니다.  ```pyside6-rcc resources.qrc -o resources_rc.py```


> **modules/ui_functions.py**: 사용자 인터페이스/GUI와 관련된 기능만 여기에 추가하십시오.

> **modules/ui_main.py**: Qt Designer에서 내보낸 사용자 인터페이스와 관련된 파일입니다. 다음 명령을 사용하여 수동으로 컴파일할 수 있습니다.  ```pyside6-uic main.ui> ui_main.py```  
.py에서 내보낸 후 "import resources_rc" 줄을 "from.Resoucers_rc import *"로 변경하여 모듈로 사용합니다.

> **images/**: Python(resources_re.py)으로 변환하기 전에 모든 이미지와 아이콘을 여기에 넣습니다.  ```pyside6-rcc resources.qrc -o resources_rc.py```

# Projects Created Using PyDracula
**See the projects that were created using PyDracula.**
> To participate create a "Issue" with the name beginning with "#pydracula_project", leaving the link of your project on Github, name of the creator and what is its functionality. Your project will be added and this list will be deleted from "Issue".
**Malicious programs will not be added**!

# pyqt_sonobuoy_gui
IVIS. Park Byung gwon