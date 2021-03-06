#include "lists.h"
int list_length(listint_t *head);
int check_arr(int *arr, int start, int end);

/**
 * is_palindrome - checks if  singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 or 0 is it
 */
int is_palindrome(listint_t **head)
{
	int i, length, arr[4096];
	listint_t *mover;

	if (!head)
		return (0);

	length = list_length(*head);

	if (length <  2)
		return (1);

	if (length == 2)
	{
		if ((*head)->n == (*head)->next->n)
			return (1);
		return (0);
	}

	mover = *head;
	for (i = 0; i < length; i++)
	{
		arr[i] = mover->n;
		mover = mover->next;
	}

	return (check_arr(arr, 0, length - 1));
}

/**
 * list_length - counts nodes in list
 * @head: pointer to list
 * Return: length of list
 */
int list_length(listint_t *head)
{
	listint_t *mover;
	int nodes = 1;

	if (!head)
		return (0);

	mover = head;
	while (mover && mover->next)
	{
		mover = mover->next;
		nodes++;
	}

	return (nodes);
}
/**
 * check_arr - recursively check if array is a palindrome
 * @arr: pointer to the array
 * @start: start index
 * @end: end index
 * Return: 1 if palindrom, 0 if not
 */
int check_arr(int *arr, int start, int end)
{
	if (arr[start] != arr[end])
		return (0);

	if (start > end)
		return (1);

	return (check_arr(arr, start + 1, end - 1));
}
