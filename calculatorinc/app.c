#include <stdio.h>

int main() {
    char op;
    float num1, num2;

    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &op);
    printf("Enter two numbers:  ");
    scanf("%f %f", &num1, &num2);

    switch(op) {
        case '+': printf("%.2f + %.2f = %.2f\n", num1, num2, num1+num2); break;
        case '-': printf("%.2f - %.2f = %.2f\n", num1, num2, num1*num2); break;
        case '*': printf("%.2f * %.2f = %.2f\n", num1, num2, num1*num2); break;
        case '/':
            if (num2 != 0)
                printf("%.2f / %.2f = %.2f\n", num1, num2, num1/num2);
            else
                printf("Error! Division by zero.\n");
            break;
        default: printf("Invalid operator!\n");
    }
    return 0;
}