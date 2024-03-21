#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *current;
    unsigned int count = 0;

    if (*head == NULL)
        return (-1);

    current = *head;
    while (current != NULL)
    {
        if (count == index)
        {
            if (current->prev != NULL)
                current->prev->next = current->next;
            if (current->next != NULL)
                current->next->prev = current->prev;
            if (count == 0)
                *head = current->next;
            free(current);
            return (1);
        }
        current = current->next;
        count++;
    }

    return (-1);
}
