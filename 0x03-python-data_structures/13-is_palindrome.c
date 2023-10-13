#include "lists.h"

/**
 * is_palindrome - checks for palindrome
 * @head: list
 * Return: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	return (check(head, *head));
}

/**
 * check - checks for palindrome
 * @head: head of the list
 * @end: last node of the list
 * Return: 1 if palindrom, 0 if not
*/
int check(listint_t **head, listint_t *end)
{
	if (!end)
		return (1);
	if (check(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
