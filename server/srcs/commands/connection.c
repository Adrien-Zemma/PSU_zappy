/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

int	send_connection(client_t **targets, client_t *origin)
{
	for (int i = 0; targets[i]; i++)
		if (targets[i]->id == -1)
			dprintf(targets[i]->fd, "pnw #%d %d %d %d %d %s\n", origin->id,
			origin->posX, origin->posY, origin->orientation,
			origin->level, origin->team);
	return OK;
}