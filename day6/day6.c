#include <stdio.h>
#include <stdlib.h>

#define CHKERR(X) do{if((X)){printf("%s: error\n",#X);return -1;}}while(0)
#define CHKALLOC(X) do{if((X)==(void*)-1){printf("%s: error\n",#X); return -1;}}while(0)

struct slice_t{
    char* buffer;
    size_t len;
};

struct slice_t read_file_as_buffer (char* fname)
{
    FILE* file = fopen(fname, "r");
    fseek(file, 0, SEEK_END);
    size_t size = ftell(file);
    char* buffer = malloc(size);
    fread(buffer, 1, size, file);
    struct slice_t slice;
    slice.buffer = buffer;
    slice.len = size;

    return slice;
}

int main(int argc, char** argv)
{
    struct slice_t file = read_file_as_buffer(char*)

    return 0;
}