#include <stdio.h>

int main()
{
  printf("Content-type: text/html\n\n");//First line in CGI,required by browser
  printf("<html>\n");
  printf("<body>\n");
  printf("<h1>Hello there!</h1>\n");
  printf("</body>\n");
  printf("</html>\n");
  return 0;
}
