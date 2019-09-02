add_executable(counter main.cpp)
target_link_libraries(counter Counter::libCounter)

# Install the counter executable during "make install".
# This variables from GNUInstallDirs included from the top CMakeLists.txt
install(TARGETS counter
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR})
