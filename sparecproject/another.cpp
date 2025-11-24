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
            break

    }
return 0;
}
