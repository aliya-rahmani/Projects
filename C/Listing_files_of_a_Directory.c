#include <stdio.h>
#include <unistd.h>
#include <dirent.h>
int main()
{
    FILE *fp;
    char *ch, s[100];
    struct dirent *de; // Pointer for directory entry

    chdir("c:\\Users\\SUBHADEEP\\Desktop");

    // opendir() returns a pointer of DIR type.
    DIR *dr = opendir(".");

    if (dr == NULL) // opendir returns NULL if couldn't open directory
    {
        printf("Could not open current directory");
        return 0;
    }
    while ((de = readdir(dr)) != NULL)
        printf("%s \n", de->d_name);

    closedir(dr);
    return 0;
}
