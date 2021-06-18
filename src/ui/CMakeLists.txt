find_package(QT NAMES Qt6 Qt5 COMPONENTS Core Quick LinguistTools REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core Quick LinguistTools REQUIRED)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

execute_process(COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/update_resource.py qml conf)

file(GLOB cpp_srcs *.cpp)
file(GLOB translations *.ts)
set(srcs ${cpp_srcs} ${translations} qt_resource.qrc)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_create_translation(QM_FILES ${CMAKE_SOURCE_DIR} ${translations})
    qt_import_qml_plugins(ui)
else()
    qt5_create_translation(QM_FILES ${CMAKE_SOURCE_DIR} ${translations})
endif()

add_library(ui ${srcs})

target_compile_definitions(ui
  PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(ui
  PRIVATE Qt${QT_VERSION_MAJOR}::Core Qt${QT_VERSION_MAJOR}::Quick)