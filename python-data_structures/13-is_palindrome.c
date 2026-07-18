#include "lists.h"
#include <stdlib.h>

listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;
    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return (prev);
}

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *mid, *reversed;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    mid = slow;
    reversed = reverse_list(&mid);

    fast = *head;
    while (reversed)
    {
        if (fast->n != reversed->n)
            return (0);
        fast = fast->next;
        reversed = reversed->next;
    }

    reverse_list(&mid);
    return (1);
}
