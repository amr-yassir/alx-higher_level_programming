#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: inserts a number into a sorted singly linked list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (new->n > current->n)
				current->next = new;
			current = current->next;
		}
	}
	return (new);
}
