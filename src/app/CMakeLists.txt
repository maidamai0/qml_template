file(GLOB srcs *.cpp)
add_executable(${CMAKE_PROJECT_NAME} WIN32 ${srcs})
target_link_libraries(${CMAKE_PROJECT_NAME} ui)

find_package(QT NAMES Qt6 Qt5 COMPONENTS Core  REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core REQUIRED)
get_target_property(qmake_executable Qt${QT_VERSION_MAJOR}::qmake IMPORTED_LOCATION)
get_filename_component(qt_bin_dir "${qmake_executable}" DIRECTORY)
find_program(WINDEPLOYQT_EXECUTABLE windeployqt HINTS "${qt_bin_dir}")
message(STATUS "WINDEPLOYQT_EXECUTABLE is ${WINDEPLOYQT_EXECUTABLE}")

set(QMLPLUGINDUMP_BIN ${qt_bin_dir}/qmlplugindump)
set(GENERATE_QMLTYPES_COMMAND ${QMLPLUGINDUMP_BIN} -nonrelocatable ui.quick 1.0 ${CMAKE_RUNTIME_OUTPUT_DIRECTORY} > ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ui/quick/plugin.qmltypes)

set(qt_deploy_cmd ${WINDEPLOYQT_EXECUTABLE} --${build_type} --qmldir ${CMAKE_CURRENT_SOURCE_DIR}/../ui $<TARGET_FILE:${CMAKE_PROJECT_NAME}>)

add_custom_command(
    TARGET ${CMAKE_PROJECT_NAME}
    POST_BUILD
    COMMAND ${QMLPLUGINDUMP_BIN} -nonrelocatable ui.quick 1.0 ${CMAKE_RUNTIME_OUTPUT_DIRECTORY} > ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/ui/quick/plugin.qmltypes
    COMMAND ${qt_deploy_cmd}
)