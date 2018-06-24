/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Main C file
*/

#include "map.h"

void	append_player(tile_t **tile, client_t *client)
{
	int i;

	for (i = 0; (*tile)->clients[i]; i++);
	(*tile)->clients = realloc((*tile)->clients,
					sizeof(client_t *) * (i + 2));
	(*tile)->clients[i] = client;
	(*tile)->clients[i + 1] = NULL;
}

int	reorganize_players(client_t ***clients, int index)
{
	int i;

	for (i = 0; (*clients)[i]; i++);
	if (index > i)
		return -1;
	index++;
	for (; (*clients)[index]; index++)
		(*clients)[index - 1] = (*clients)[index];
	*clients = realloc(*clients, sizeof(client_t *) * (index));
	(*clients)[index - 1] = NULL;
	return (index - 1);
}

void	manage_tile(tile_t *tile, client_t *client)
{
	for (int k = 0; tile->clients[k]; k++) {
		if (tile->clients[k] == client) {
			reorganize_players(&tile->clients, k);
			break;
		}
	}
}

int	remove_player(tile_t ***map, client_t *client)
{
	for (int i = 0; map[i]; i++) {
		for (int j = 0; map[i][j]; j++) {
			manage_tile(map[i][j], client);
		}
	}
	return OK;
}
