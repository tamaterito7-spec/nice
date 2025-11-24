#include <iostream>

using namespace std;

int main(){
    int no_of_likes = 10;
    switch(no_of_likes){
        case 10:
            cout << "Performing Good!!" << endl;
            break;
        case 100:
            cout << "That's the target" << endl;
        default:
            cout << "Not enough Information";
            break;
//THIS IS A SAMPLE COMMENT
/*
THIS IS A MULTILINE COMMENT
IT SPANS SEVERAL LINES
AND IS USED FOR WRITING LONGER
COMMENTS
*/
    }
return 0;
}
