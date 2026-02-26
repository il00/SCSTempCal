# SCSTempCal

**SCSTempCal** is a software tool for theoretical estimation of the maximum temperature achieved in combustion reactions, specifically designed for Solution Combustion Synthesis (SCS) and Self-Propagating High-Temperature Synthesis (SHS).

*Read this in other languages: [English](#english) | [Русский](#русский)*

---

## <a name="english"></a>English 🇬🇧

### About The Program

SCSTempCal allows researchers to model reactions using different types of fuels and various product compositions, enabling both qualitative and quantitative assessment of the temperature regime in combustion processes. The calculation algorithm employs assumptions that make it valid for combustion processes lasting up to 15-20 seconds.

#### Key Features
- **Four approximation levels** for temperature estimation
- **Multiple reaction pathway simulation** capabilities
- **Applicability** for both SCS and SHS reactions
- **User-friendly graphical interface** for easy data input and result visualization
- **Substance library** with thermodynamic constants

### Getting Started

#### Prerequisites

**For executable file (.exe):**
- Windows XP or newer

**For running from source code (.py):**
- Python 3.4+ interpreter
- Required libraries: `numpy`, `matplotlib`, `tkinter` (or `python3-tk` on Linux)
- Supported OS: Windows, Linux, macOS

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/SCSTempCal.git
```
2. **Choose your language version**:  
Navigate to the `SCSTempCal_en` folder for the English version  
Navigate to the `SCSTempCal_ru` for the Russian version  

**Option A: Windows Users (Executable)**

Simply run `SCSTempCal.exe` — no installation required.

**Option B: Run from Source (Cross-platform)**
```bash
python SCSTempCal.py
```
### Repository Contents

|File                     |Description                     |
|-------------------------|--------------------------------|
|`SCSTempCal.py`          |Python source code              |
|`SCSTempCal.exe`         |Executable file for Windows     |
|`fig.png`                |Start screen image              |
|`substance_library.txt`  |Thermodynamic constants database|
|`input.txt`              |Sample input file               |
|`SCSTempCal_manual.pdf`  |User manual                     |
|`SCSTempCal_manual.docx` |User manual                     |
|`References of data.pdf` |Data sources                    |
|`References of data.docx`|Data sources                    |

### Citation

When publishing results obtained with this software, please cite:

1. **Original research article:**

    [Khaliullin, Sh.M., Popov, I.S. & Zhuravlev, V.D. SCSTempCal Software for Solution-Combustion-Synthesis Applications. Int J Self-Propag High-Temp Synth 29, 87–95 (2020).](https://link.springer.com/article/10.3103/S1061386220020077)  
   DOI: 10.3103/S1061386220020077

2. **Software registration certificate:**

    [https://elibrary.ru/item.asp?id=42710212](https://elibrary.ru/item.asp?id=42710212)

### Authors

Sh.M. Khaliullin — development of thermodynamic model and calculation algorithm  
I.S. Popov — program implementation  
V.D. Zhuravlev — project supervision, critical review  

### License

This software is provided for free use. When using the program, please cite the relevant publications.

## <a name="русский"></a>Русский 🇷🇺

### О программе

**SCSTempCal** — программа для теоретической оценки максимальной температуры, достигаемой в реакциях горения, предназначенная для синтеза горением растворов (Solution Combustion Synthesis — SCS) и самораспространяющегося высокотемпературного синтеза (СВС / SHS).

Программа позволяет моделировать реакции с использованием различных видов топлива и различным составом продуктов, давая возможность как качественной, так и количественной оценки температурного режима процессов горения. Алгоритм расчета основан на допущениях, которые позволяют корректно вычислять температуры для процессов длительностью до 15–20 секунд.

#### Ключевые возможности
- **Четыре уровня приближения** для оценки температуры
- **Моделирование различных путей** протекания реакций
- **Применение** для SCS и СВС-реакций
- **Удобный графический интерфейс** для ввода данных и визуализации результатов
- **Библиотека веществ** с термодинамическими константами

### Начало работы
#### Требования

**Для исполняемого файла (.exe):**
- Windows XP или новее

**Для запуска из исходного кода (.py):**
- Интерпретатор Python версии 3.4 или выше
- Библиотеки: numpy, matplotlib, tkinter (или python3-tk на Linux)
- Поддерживаемые ОС: Windows, Linux, macOS

### Установка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/your-username/SCSTempCal.git
```
2. **Выберите версию программы:**

Папка `SCSTempCal_en` для английской версии

Папка `SCSTempCal_ru` для русской версии

**Вариант A: Windows (исполняемый файл)**

Запустите SCSTempCal.exe — установка не требуется.

**Вариант Б: Запуск из исходного кода**
```bash
python SCSTempCal.py
```

### Содержимое репозитория

|Файл                   	|Описание                          |
|-------------------------|----------------------------------|
|`SCSTempCal.py`          |Исходный код на Python            |
|`SCSTempCal.exe`        	|Исполняемый файл для Windows      |
|`fig.png`                |Изображение для главного экрана   |
|`substance_library.txt`  |База термодинамических констант   |
|`input.txt`              |Пример входного файла             |
|`SCSTempCal_manual.pdf`  |Инструкция                        |
|`SCSTempCal_manual.docx` |Инструкция                        |
|`Referenced of data.pdf`	|Источники термодинамических данных|
|`Referenced of data.docx`|Источники термодинамических данных|


### Цитирование

При публикации результатов, полученных с помощью программы, пожалуйста, ссылайтесь на:

1. **Публикацию в журнале:**

    [Khaliullin, Sh.M., Popov, I.S. & Zhuravlev, V.D. SCSTempCal Software for Solution-Combustion-Synthesis Applications. Int J Self-Propag High-Temp Synth 29, 87–95 (2020).](https://link.springer.com/article/10.3103/S1061386220020077)  
   DOI: 10.3103/S1061386220020077

2. **Свидетельство о регистрации:**

    [https://elibrary.ru/item.asp?id=42710212](https://elibrary.ru/item.asp?id=42710212)

### Авторы

Ш.М. Халиуллин — создание термодинамической модели и алгоритма расчета  
И.С. Попов — разработка программного обеспечения  
В.Д. Журавлев — руководство проектом, критика и советы  

### Лицензия

Программа предоставляется для свободного использования. При использовании программы, пожалуйста, цитируйте соответствующие публикации.
