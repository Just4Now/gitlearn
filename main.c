#include <stdio.h>
#include <termios.h>
#include <string.h>
int main()
{
int c;
int w,h;
struct termios new_setting,init_setting;
   
    if (tcgetattr(0, &init_setting) != 0)
    {
        printf("Cannot get the attribution of the terminal.");
        goto quit;
    }
memcpy(&new_setting, &init_setting, sizeof(struct termios));

    new_setting.c_lflag &= ~(ICANON | ECHO);;
    if (tcsetattr(0, TCSANOW, &new_setting) != 0)
    {
        printf("Cannot set the attribution of the terminal.");
        goto quit;
    }
                do
                {
                    printf("---- Enter space to display more records or 'q' to quit. ----\n");
                    c = getchar();
if (c == 'q') {
                        goto quit;
                    }else if (c == ' ') {
                        break;
                    }else
                    {
                        /* do nothing */
                    }                    


                } while (c != EOF);
quit:
if (tcsetattr(0, TCSANOW, &init_setting) != 0)
    {
        printf("Cannot set the attribution of the terminal.");
    }
return 0;
}
