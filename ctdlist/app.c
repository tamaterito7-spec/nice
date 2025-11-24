#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define FILENAME "tasks.txt"
#define INIT_CAP 8
#define DESC_MAX 256

typedef struct {
    int id;
    char desc[DESC_MAX];
    int done;
} Task;

Task *tasks = NULL;
int task_count = 0;
int capacity = 0;
int next_id = 1;

void trim_newline(char *s) {
    char *p = strchr(s, '\n');
    if (p) *p = '\0';
}

void grow_array(void) {
    int new_cap = capacity ? capacity * 2 : INIT_CAP;
    Task *tmp = realloc(tasks, new_cap * sizeof(Task));
    if (!tmp) {perror("realloc"); exit(EXIT_FAILURE); }
    tasks = tmp;
    capacity = new_cap;
}

void load_tasks(void) {
    FILE *fp = fopen(FILENAME, "r");
    if (!fp) return;

    char line[512];
    while (fgets(line, sizeof(line), fp)) {
        char *tok = strtok(line, "|");
        if (!tok) continue;
        int id = atoi(tok);

        tok = strtok(NULL, "|");
        if (!tok) continue;
        strncpy(tasks[task_count].desc, tok, DESC_MAX-1);
        tasks[task_count].desc[DESC_MAX-1] = '\0';

        tok = strtok(NULL, "|");
        if (!tok) continue;
        tasks[task_count].done = atoi(tok);

        tasks[task_count].id = id;
        task_count++;
        if (id >= next_id) next_id = id + 1;
        
        if (task_count == capacity) grow_array();
    }
    fclose(fp);
}

void save_tasks(void) {
    FILE *fp = fopen(FILENAME, "w");
    if (!fp) { perror("fopen save"); return; }

    for (int i = 0; i < task_count; ++i) {
        fprintf(fp, "%d|%s|%d\n",
                tasks[i].id,
                tasks[i].desc,
                tasks[i].done);
    }
    fclose(fp);
}

void add_task(void) {
    grow_array();

    printf("Enter task description: ");
    if (!fgets(tasks[task_count].desc, DESC_MAX, stdin)) return;
    trim_newline(tasks[task_count].desc);

    tasks[task_count].id = next_id++;
    tasks[task_count].done = 0;
    task_count++;

    printf("Task added (ID %d).\n", tasks[task_count-1].id);
}

void list_tasks(void) {
    if (task_count == 0) {
        printf("No tasks yet.\n");
        return;
    }
    printf("\n=== To-Do List===\n");
    for (int i = 0; i < task_count; ++i) {
        printf("%c %3d. %s\n",
        tasks[i].done ? "[X]" : "[ ]",
        tasks[i].id,
        tasks[i].desc);
    }
    printf("===================\n\n");
}

void mark_done(void) {
    printf("Enter task ID to mark as done: ");
    int id;
    if (scanf("%d", &id) != 1) {
        while (getchar() != '\n');
        printf("Invalid input.\n");
        return;
    }
    while (getchar() != '\n');
   
    for (int i = 0; i < task_count; ++i) {
        if (tasks[i].id == id) {
            tasks[i].done = 1;
            printf("Task %d marked as done.\n", id);
            return;
        }
    }
    printf("Task ID %d not found.\n", id);
}

void delete_task(void) {
    printf("Enter task ID to delete: ");
    int id;
    if (scanf("%d", &id) != 1) {
        while (getchar() != '\n');
        printf("Invalid input.\n");
        return;
    }
    while (getchar() != '\n');

    for (int i = 0; i < task_count; ++i) {
        if (tasks[i].id == id) {
            memmove(&tasks[i], &tasks[i+1],
            (task_count - i - 1) * sizeof(Task));
            task_count--;
            printf("Task %d deleted.\n", id);
            return;
        }
    }
    printf("Task ID %d not found.\n", id);
}

int main(void) {
    grow_array();
    load_tasks();

    while (1) {
        printf("\n--- To-Do Manager ---\n");
        printf("1) Add Task\n");
        printf("2) List Tasks\n");
        printf("3) Mark task done\n");
        printf("4) Delete task\n");
        printf("5) Quit \n");
        printf("Choice: ");

        int choice;
        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');
            printf("Please enter a number.\n");
            continue;
        }
        while (getchar() != '\n');

        switch (choice) {
            case 1: add_task(); break;
            case 2: list_tasks(); break;
            case 3: mark_done(); break;
            case 4: delete_task(); break;
            case 5:
            save_tasks();
            free(tasks);
            printf("Goodbye!\n");        
            return 0;
        default:
        printf("Invalid option.\n");
        }
    }
}