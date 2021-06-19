file(GLOB srcs *.cpp)
add_executable(${CMAKE_PROJECT_NAME} ${srcs})
target_link_libraries(${CMAKE_PROJECT_NAME} ui)

find_package(QT NAMES Qt6 Qt5 COMPONENTS Core  REQUIRED)
find_package(Qt${QT_VERSION_MAJOR} COMPONENTS Core REQUIRED)
get_target_property(qmake_executable Qt${QT_VERSION_MAJOR}::qmake IMPORTED_LOCATION)
get_filename_component(qt_bin_dir "${qmake_executable}" DIRECTORY)
find_program(WINDEPLOYQT_EXECUTABLE windeployqt HINTS "${qt_bin_dir}")
message(STATUS "WINDEPLOYQT_EXECUTABLE is ${WINDEPLOYQT_EXECUTABLE}")

if (CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(deploy_v --debug)
else()
    set(deploy_v --release)
endif()

add_custom_command(
    TARGET ${CMAKE_PROJECT_NAME}
    POST_BUILD
    COMMAND ${WINDEPLOYQT_EXECUTABLE} ${deploy_v} --qmldir ${CMAKE_CURRENT_SOURCE_DIR}/../ui $<TARGET_FILE:${CMAKE_PROJECT_NAME}>
)
