#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include<string.h>

#define MAX_STATES 1000

typedef struct {
    int jug1_amount;
    int jug2_amount;
} State;

bool water_jug(int jug1_capacity, int jug2_capacity, int target) {
    State queue[MAX_STATES];
    int front = 0, rear = 0;
    bool visited[jug1_capacity + 1][jug2_capacity + 1];
    memset(visited, false, sizeof(visited));

    // Starting state: both jugs are empty
    queue[rear].jug1_amount = 0;
    queue[rear].jug2_amount = 0;
    rear++;

    while (front < rear) {
        State current = queue[front];
        front++;

        if (current.jug1_amount == target || current.jug2_amount == target) {
            return true;
        }

        // Action: Fill jug1
        if (!visited[jug1_capacity][current.jug2_amount]) {
            queue[rear].jug1_amount = jug1_capacity;
            queue[rear].jug2_amount = current.jug2_amount;
            rear++;
            visited[jug1_capacity][current.jug2_amount] = true;
        }

        // Action: Fill jug2
        if (!visited[current.jug1_amount][jug2_capacity]) {
            queue[rear].jug1_amount = current.jug1_amount;
            queue[rear].jug2_amount = jug2_capacity;
            rear++;
            visited[current.jug1_amount][jug2_capacity] = true;
        }

        // Action: Empty jug1
        if (!visited[0][current.jug2_amount]) {
            queue[rear].jug1_amount = 0;
            queue[rear].jug2_amount = current.jug2_amount;
            rear++;
            visited[0][current.jug2_amount] = true;
        }

        // Action: Empty jug2
        if (!visited[current.jug1_amount][0]) {
            queue[rear].jug1_amount = current.jug1_amount;
            queue[rear].jug2_amount = 0;
            rear++;
            visited[current.jug1_amount][0] = true;
        }

        // Action: Pour jug1 into jug2 until jug2 is full or jug1 is empty
        int pour_amount = (current.jug1_amount <= jug2_capacity - current.jug2_amount) ? current.jug1_amount : jug2_capacity - current.jug2_amount;
        if (!visited[current.jug1_amount - pour_amount][current.jug2_amount + pour_amount]) {
            queue[rear].jug1_amount = current.jug1_amount - pour_amount;
            queue[rear].jug2_amount = current.jug2_amount + pour_amount;
            rear++;
            visited[current.jug1_amount - pour_amount][current.jug2_amount + pour_amount] = true;
        }

        // Action: Pour jug2 into jug1 until jug1 is full or jug2 is empty
        pour_amount = (current.jug2_amount <= jug1_capacity - current.jug1_amount) ? current.jug2_amount : jug1_capacity - current.jug1_amount;
        if (!visited[current.jug1_amount + pour_amount][current.jug2_amount - pour_amount]) {
            queue[rear].jug1_amount = current.jug1_amount + pour_amount;
            queue[rear].jug2_amount = current.jug2_amount - pour_amount;
            rear++;
            visited[current.jug1_amount + pour_amount][current.jug2_amount - pour_amount] = true;
        }
    }

    return false;
}

int main() {
    int jug1_capacity = 5;
    int jug2_capacity = 7;
    int target = 3;
    bool result = water_jug(jug1_capacity, jug2_capacity, target);
    printf("Result: %s\n", result ? "Passed" : "Falied");
    return 0;
}
