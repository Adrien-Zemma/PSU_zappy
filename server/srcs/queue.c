/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Queue functions
*/

#include "server.h"
#include "commands.h"

command_t	**queue_init(void)
{
	command_t	**queue = malloc(sizeof(command_t *));
	if (!queue)
		return NULL;
	queue[0] = NULL;
	return (queue);
}

void	queue_append(command_t ***queue, command_t *command)
{
	int i;

	for (i = 0; (*queue)[i]; i++);
	if (i >= 10) {
		dprintf(2, "Queue is full\n");
		return;
	}
	(*queue) = realloc(*queue, sizeof(command_t *) * (i + 2));
	(*queue)[i] = command;
	(*queue)[i + 1] = NULL;
}

command_t	*queue_get(command_t ***queue)
{
	command_t	*to_ret = (*queue)[0];
	return (to_ret);
}

command_t	*queue_pop(command_t ***queue)
{
	command_t	*to_ret = NULL;
	int i;
	int index;

	for (i = 0; (*queue)[i]; i++);
	if (i <= 0)
		return NULL;
	to_ret = (*queue)[0];
	for (index = 1; (*queue)[index]; index++) {
		(*queue)[index - 1] = (*queue)[index];
	}
	*queue = realloc(*queue, sizeof(client_t *) * (index));
	(*queue)[index - 1] = NULL;
	return (to_ret);
}
