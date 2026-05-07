# Qt/C++桌面应用开发 Agent编写规则
# 适用场景：Qt、C++、PyQt、桌面应用

# ============================================
# 技术栈定义
# ============================================
tech_stack:
  language: "C++17 / Python 3.x"
  framework: "Qt 5.15+ / Qt 6.x"
  build_system:
    - "CMake"
    - "qmake"
  ide:
    - "Qt Creator"
    - "Visual Studio"
    - "CLion"
  ui_design: "Qt Designer (.ui文件)"
  python_binding: "PyQt6 / PySide6"

# ============================================
# Agent角色能力模板
# ============================================
capabilities_template:
  core_skills:
    - skill: "Qt界面开发"
      level: "expert"
      components:
        - "QMainWindow主窗口开发"
        - "QWidget自定义控件"
        - "QDialog对话框开发"
        - "QMenu菜单栏与工具栏"
        - "QStatusBar状态栏"

    - skill: "Qt布局管理"
      level: "expert"
      components:
        - "QVBoxLayout垂直布局"
        - "QHBoxLayout水平布局"
        - "QGridLayout网格布局"
        - "QFormLayout表单布局"
        - "QStackedLayout堆叠布局"

    - skill: "Qt信号槽机制"
      level: "expert"
      components:
        - "signals/slots声明与定义"
        - "connect连接方式（新式/旧式）"
        - "lambda表达式槽函数"
        - "信号槽跨线程通信"
        - "自定义信号槽"

    - skill: "Qt模型视图架构"
      level: "advanced"
      components:
        - "QAbstractItemModel自定义模型"
        - "QTableView/QListView/QTreeView视图"
        - "QItemDelegate/QStyledItemDelegate委托"
        - "QSortFilterProxyModel代理模型"

    - skill: "Qt多线程"
      level: "advanced"
      components:
        - "QThread线程管理"
        - "QThreadPool线程池"
        - "QtConcurrent并发框架"
        - "QMutex/QReadWriteLock同步"

    - skill: "Qt网络编程"
      level: "intermediate"
      components:
        - "QTcpSocket/TCP通信"
        - "QUdpSocket/UDP通信"
        - "QNetworkAccessManager HTTP"
        - "QSslSocket加密通信"

# ============================================
# 项目结构规范
# ============================================
project_structure:
  cmake_project: |
    {project_name}/
    ├── CMakeLists.txt              # CMake配置
    ├── src/
    │   ├── main.cpp                # 主入口
    │   ├── mainwindow.cpp/.h/.ui   # 主窗口
    │   ├── widgets/                # 自定义控件
    │   │   ├── customwidget.cpp/.h
    │   │   ├── statuswidget.cpp/.h/.ui
    │   ├── models/                 # 数据模型
    │   │   ├── tablemodel.cpp/.h
    │   │   ├── treemodel.cpp/.h
    │   ├── dialogs/                # 对话框
    │   │   ├── settingsdialog.cpp/.h/.ui
    │   │   ├── aboutdialog.cpp/.h/.ui
    │   ├── utils/                  # 工具类
    │   │   ├── helper.cpp/.h
    │   │   ├── logger.cpp/.h
    │   ├── network/                # 网络模块
    │   │   ├── tcpclient.cpp/.h
    │   │   ├── httpclient.cpp/.h
    │   └── resources/              # 资源文件
    │       ├── icons.qrc
    │       ├── images/
    │       ├── translations/
    ├── include/                    # 头文件（可选）
    ├── tests/                      # 单元测试
    ├── docs/                       # 文档
    └── README.md

  qmake_project: |
    {project_name}/
    ├── {project_name}.pro          # qmake项目文件
    ├── main.cpp
    ├── mainwindow.cpp/.h/.ui
    ├── widgets/
    ├── models/
    ├── dialogs/
    ├── utils/
    ├── resources/
    │   ├── resources.qrc
    └── README.md

  pyqt_project: |
    {project_name}/
    ├── src/
    │   ├── main.py                 # 主入口
    │   ├── main_window.py          # 主窗口
    │   ├── widgets/                # 自定义控件
    │   │   ├── custom_widget.py
    │   │   ├── status_widget.py
    │   ├── models/                 # 数据模型
    │   │   ├── table_model.py
    │   ├── dialogs/                # 对话框
    │   │   ├── settings_dialog.py
    │   ├── utils/                  # 工具类
    │   │   ├── helper.py
    │   └── resources/              # 资源文件
    │       ├── icons/
    ├── ui/                         # UI文件
    │   ├── main_window.ui
    │   ├── settings_dialog.ui
    ├── requirements.txt
    ├── setup.py
    └── README.md

# ============================================
# 命名规范
# ============================================
naming_conventions:
  # 类命名
  classes:
    - rule: "PascalCase（大驼峰）"
      examples: ["MainWindow", "DataModel", "CustomWidget"]
    - rule: "Widget类以Widget结尾"
      examples: ["TableWidget", "TreeWidget", "StatusWidget"]
    - rule: "Dialog类以Dialog结尾"
      examples: ["SettingsDialog", "AboutDialog", "LoginDialog"]
    - rule: "Model类以Model结尾"
      examples: ["TableModel", "TreeModel", "ListModel"]

  # 文件命名
  files:
    - rule: "类名与文件名对应（C++）"
      examples: ["mainwindow.cpp/mainwindow.h/mainwindow.ui"]
    - rule: "Python文件小写+下划线"
      examples: ["main_window.py", "custom_widget.py"]

  # 信号槽命名
  signals_slots:
    signals:
      - rule: "以信号含义命名，不加前缀"
        examples: ["clicked()", "dataChanged()", "errorOccurred()", "progressUpdated(int)"]
    slots:
      - rule: "on前缀 + 触发源 + 事件（自动连接）"
        examples: ["onButtonClicked()", "onDataChanged()"]
      - rule: "普通槽函数直接用含义命名"
        examples: ["updateData()", "handleError()", "processResult()"]

  # 变量命名
  variables:
    - rule: "成员变量m_前缀（C++）"
      examples: ["m_data", "m_model", "m_widget", "m_tcpClient"]
    - rule: "局部变量小驼峰（C++）或小写下划线（Python）"
      examples: ["currentIndex", "selectedItem"]
    - rule: "常量k前缀或全大写"
      examples: ["kMaxSize", "MAX_COUNT", "kDefaultTimeout"]
    - rule: "全局变量g_前缀"
      examples: ["g_config", "g_logger"]

  # Qt类型命名
  qt_types:
    - rule: "使用Qt类型而非标准库（部分场景）"
      examples:
        - "QString而非std::string"
        - "QList/QVector而非std::vector"
        - "QMap而非std::map"
        - "QDateTime而非std::chrono"

# ============================================
# 代码风格规范
# ============================================
code_style:
  # Qt主窗口模板
  main_window: |
    class MainWindow : public QMainWindow {
        Q_OBJECT

    public:
        explicit MainWindow(QWidget *parent = nullptr);
        ~MainWindow();

    private slots:
        void onNewFile();
        void onOpenFile();
        void onSaveFile();
        void onExit();
        void onAbout();

    private:
        void setupUi();
        void setupMenuBar();
        void setupToolBar();
        void setupStatusBar();
        void setupConnections();

        Ui::MainWindow *ui;
    };

    // mainwindow.cpp
    MainWindow::MainWindow(QWidget *parent)
        : QMainWindow(parent)
        , ui(new Ui::MainWindow)
    {
        ui->setupUi(this);
        setupMenuBar();
        setupToolBar();
        setupStatusBar();
        setupConnections();
    }

    void MainWindow::setupConnections() {
        // 新式connect（推荐）
        connect(ui->newButton, &QPushButton::clicked, this, &MainWindow::onNewFile);
        connect(ui->openButton, &QPushButton::clicked, this, &MainWindow::onOpenFile);
        
        // lambda槽函数
        connect(ui->saveButton, &QPushButton::clicked, this, [this]() {
            if (m_currentFile.isEmpty()) {
                onSaveAs();
            } else {
                saveFile(m_currentFile);
            }
        });
    }

  # 自定义Widget模板
  custom_widget: |
    class CustomWidget : public QWidget {
        Q_OBJECT

    public:
        explicit CustomWidget(QWidget *parent = nullptr);
        ~CustomWidget();

        void setData(const QVariant &data);
        QVariant data() const;

    signals:
        void dataChanged();
        void errorOccurred(const QString &message);

    private slots:
        void onInternalUpdate();

    private:
        void setupLayout();
        void updateDisplay();

        QVBoxLayout *m_layout;
        QLabel *m_label;
        QLineEdit *m_edit;
        QVariant m_data;
    };

  # 数据模型模板
  table_model: |
    class TableModel : public QAbstractTableModel {
        Q_OBJECT

    public:
        explicit TableModel(QObject *parent = nullptr);
        explicit TableModel(const QList<DataItem> &data, QObject *parent = nullptr);

        // 必须实现的虚函数
        int rowCount(const QModelIndex &parent = QModelIndex()) const override;
        int columnCount(const QModelIndex &parent = QModelIndex()) const override;
        QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;
        QVariant headerData(int section, Qt::Orientation orientation, int role) const override;

        // 可选实现的虚函数
        bool setData(const QModelIndex &index, const QVariant &value, int role = Qt::EditRole) override;
        Qt::ItemFlags flags(const QModelIndex &index) const override;

        void setData(const QList<DataItem> &data);
        void clear();

    private:
        QList<DataItem> m_data;
        QStringList m_headers;
    };

  # PyQt模板
  pyqt_component: |
    from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
    from PyQt6.QtCore import pyqtSignal, pyqtSlot

    class CustomWidget(QWidget):
        # 信号定义
        dataChanged = pyqtSignal(object)
        errorOccurred = pyqtSignal(str)

        def __init__(self, parent=None):
            super().__init__(parent)
            self._data = None
            self._setup_ui()
            self._setup_connections()

        def _setup_ui(self):
            layout = QVBoxLayout(self)
            
            self._label = QLabel("Data Display")
            layout.addWidget(self._label)
            
            self._button = QPushButton("Update")
            layout.addWidget(self._button)

        def _setup_connections(self):
            self._button.clicked.connect(self._on_button_clicked)

        @pyqtSlot()
        def _on_button_clicked(self):
            self.dataChanged.emit(self._data)

        def set_data(self, data):
            self._data = data
            self._label.setText(str(data))
            self.dataChanged.emit(data)

        def data(self):
            return self._data

# ============================================
# Skill示例
# ============================================
skill_examples:
  qt_scaffold:
    id: "qt-scaffold"
    name: "Qt项目脚手架"
    description: "生成Qt CMake项目结构，包含主窗口、菜单、工具栏模板"

  qt_widget_generator:
    id: "qt-widget-generator"
    name: "Qt控件生成"
    description: "根据需求生成自定义QWidget控件代码"

  qt_model_generator:
    id: "qt-model-generator"
    name: "Qt模型生成"
    description: "生成QAbstractItemModel数据模型代码"

  qt_signal_slot_designer:
    id: "qt-signal-slot-designer"
    name: "Qt信号槽设计"
    description: "设计Qt信号槽连接关系和代码"

  pyqt_scaffold:
    id: "pyqt-scaffold"
    name: "PyQt项目脚手架"
    description: "生成PyQt/PySide项目结构"

# ============================================
# 注意事项
# ============================================
notes:
  - "Qt项目必须明确设置Q_OBJECT宏才能使用信号槽"
  - "UI文件(.ui)由Qt Designer生成，不要手动修改"
  - "跨线程通信必须使用Qt::QueuedConnection"
  - "避免在槽函数中执行耗时操作，应使用线程"
  - "使用Qt官方文档作为首要参考"
  - "Qt6与Qt5有部分API差异，注意版本兼容"
  - "成员变量使用m_前缀避免命名冲突"
  - "使用新式connect语法（函数指针）"
  - "Qt对象树自动管理子对象内存"