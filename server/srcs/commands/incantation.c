/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

const tile_t level_requirement[6] {
	{1, 1, 0, 0, 0, 0, 0, NULL},
	{2, 1, 1, 1, 0, 0, 0, NULL},
	{2, 2, 0, 1, 0, 2, 0, NULL},
	{4, 1, 1, 2, 0, 1, 0, NULL},
	{4, 1, 2, 1, 3, 0, 0, NULL},
	{6, 1, 2, 3, 0, 1, 0, NULL},
	{6, 2, 2, 2, 2, 2, 1, NULL},
}

int	start_incantation(server_t *server, client_t *client, char *str)
{
	
	return OK;
}