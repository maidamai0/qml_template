get_filename_component(lib_name ${CMAKE_CURRENT_SOURCE_DIR} NAME)

find_package(QT NAMES Qt6 Qt5 COMPONENTS Core Quick LinguistTools REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core Quick LinguistTools REQUIRED)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(QML_IMPORT_PATH ${CMAKE_RUNTIME_OUTPUT_DIRECTORY} CACHE STRING "Qt Creator extra qml import paths")

file(GLOB srcs *.cpp)

add_library(${lib_name} SHARED ${srcs})

target_compile_definitions(${lib_name}
  PRIVATE $<$<OR:$<CONFIG:Debug>,$<CONFIG:RelWithDebInfo>>:QT_QML_DEBUG>)
target_link_libraries(${lib_name}
  PRIVATE Qt${QT_VERSION_MAJOR}::Core Qt${QT_VERSION_MAJOR}::Quick)
set_target_properties(
  ${lib_name}
  PROPERTIES
  RUNTIME_OUTPUT_DIRECTORY ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ui/quick
)

# During plugin searching Qt will be looking for 'qmldir' file
# So we should place it next to our plugin lib.
add_custom_command(
  TARGET ${lib_name}
  POST_BUILD
  COMMAND
      ${CMAKE_COMMAND} -E copy
      ${CMAKE_CURRENT_LIST_DIR}/qmldir
      $<TARGET_FILE_DIR:${lib_name}>/qmldir
)