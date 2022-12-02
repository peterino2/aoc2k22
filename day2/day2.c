#include <stdio.h>
#include <stdlib.h>

#define CHECK_ERR(X) do{if((X)) {printf("expression: %s has error\n", #X); return -1;}}while(0)
#define CHECK_ALLOC(X) do{if((X) == (void*)-1) {printf("unable to allocate: %s has error\n", #X); return -1;}}while(0)
int main(int argc, char** argv )
{
    FILE* f = fopen("day2.input", "r");
    char* b = NULL;
    size_t buf_size;

    if(f == NULL)
    {
        printf("Unable to open file\n");
        return -1;
    }
    CHECK_ERR(fseek(f, 0, SEEK_END));
    buf_size = ftell(f) + 1;
    CHECK_ALLOC(b = malloc(buf_size));
    CHECK_ERR(fseek(f, 0, SEEK_SET));
    fread(b, 1, buf_size, f);
    int i = 0;
    int score = 0;
    int first = 1;
    char* names[3] = {"rock", "paper", "scissor"};
    while(i < buf_size)
    {
        int op = b[i] - 'A';
        int me = b[i+2] - 'X';
        int delta = me + 1;
        if(((op + 1) % 3) == me)
        {
            delta += 6;
        }
        else if(op == me)
        {
            delta += 3;
        }

        score += delta;
        i+=4;
    }
    printf("score=%d\n", score);
    i = 0;
    score = 0;
    while(i < buf_size)
    {
        int op = b[i] - 'A';
        int res = b[i+2] - 'X';
        int d = op + 1 + 3;
        if(res == 0)
        {
            d = (op > 0 ? op - 1 : 2) + 1;
        }
        else if(res == 2)
        {
            d = ((op + 1) % 3) + 6 + 1;
        }
        score += d;
        i += 4;
    }
    printf("score = %d", score);

    free(b);
    fclose(f);
    return 0;
}
