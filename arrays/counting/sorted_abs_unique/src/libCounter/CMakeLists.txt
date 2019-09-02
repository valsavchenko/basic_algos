add_library(libCounter
            Counter.h Counter.cpp)

# CMake automatically prefixes our target name with "lib" for libraries, i.e. the built target
# will by default be called "liblibCounter.a". We adjust the library name so it becomes
# "libCounter.a" for cosmetic reasons.
set_target_properties(libCounter PROPERTIES PREFIX "")

# This adds the current source directory as an include directory for consumers of our library.
# If we have generated headers we would also add CMAKE_CURRENT_BINARY_DIR.
target_include_directories(libCounter INTERFACE $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>)

# We are using C++17 features (and so will all users of this library)
target_compile_features(libCounter PUBLIC cxx_std_17)

# Add a target in our namespace
add_library(Counter::libCounter ALIAS libCounter)
