# STM_flasher

## Requirements:
* OpenOCD (https://github.com/xpack-dev-tools/openocd-xpack/releases)
* STM32CubeMx (optional)
* Python3

## Usage
To flash STM32 you need executable file or source code of whole project.

To flash device use script flash.py
* Linux:
```bash
./flash.py -b stm32f1 -f project.elf
```

* Windows
```bash
python flash.py -b stm32f1 -f project.elf
```

If you just have source code first you need STM32CubeMX from ST (see https://www.st.com/en/development-tools/stm32cubemx.html) to generate required library or files and compile whole project.



