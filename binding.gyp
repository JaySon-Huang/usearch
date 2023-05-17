{
    "targets": [
        {
            "target_name": "usearch",
            "sources": [
                "javascript/lib.cpp"
            ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
                "include",
                "src",
                "fp16/include",
                "simsimd/include"
            ],
            "dependencies": [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            "cflags": ["-fexceptions", "-Wunknown-pragmas", "-std=c99"],
            "cflags_cc": ["-fexceptions", "-Wunknown-pragmas", "-std=c++11"],
            "xcode_settings": {
                "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                "CLANG_CXX_LIBRARY": "libc++",
                "MACOSX_DEPLOYMENT_TARGET": "10.15"
            },
            "msvs_settings": {
                "VCCLCompilerTool": { 
                    "ExceptionHandling": 1, 
                    "AdditionalOptions": [ "-std:c++11" ]
                }
            }
        }
    ]
}
