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

	if (!(*tile)->clients) {
		(*tile)->clients = malloc(sizeof(client_t *) * 1);
		(*tile)->clients[0] = NULL;
	}	
	for (i = 0; (*tile)->clients[i]; i++);
	(*tile)->clients = realloc((*tile)->clients, sizeof(client_t *) * (i + 2));
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
	// for (i = 0; (*tile)->clients[i] && (*tile)->clients[i] != client; i++);
	// if (!(*tile)->clients[i])
	// 	return KO;
	// reorganize_players(&(*tile)->clients, i);
	return OK;
}

void	search_players(tile_t ***map)
{
	for (int i = 0; map[i]; i++)
		for (int j = 0; map[i][j]; j++) {
			for (int k = 0; map[i][j]->clients[k]; k++) {
				printf("map[%d][%d][%d]:%d\n", i, j, k, map[i][j]->clients[k]->id);
			}
	}
	fflush(NULL);
}

static void	gen_tile(tile_t **node)
{
	(*node)->linemate = ADD_MINERAL(0, 2);
	(*node)->deraumere = ADD_MINERAL(0, 2);
	(*node)->sibur = ADD_MINERAL(0, 2);
	(*node)->mendiane = ADD_MINERAL(0, 2);
	(*node)->phiras = ADD_MINERAL(0, 2);
	(*node)->thystam = ADD_MINERAL(0, 2);
	(*node)->food = ADD_MINERAL(0, 2);
	(*node)->clients = malloc(sizeof(client_t *) * 1);
	(*node)->clients[0] = NULL;
}

static tile_t	**gen_line(int w)
{
	tile_t	**node = malloc(sizeof(tile_t *) * (w + 1));

	if (!node)
		return NULL;
	for (int i = 0; i < w; i++) {
		node[i] = malloc(sizeof(tile_t));
		if (!node[i])
			return NULL;
		gen_tile(&node[i]);
	}
	node[w] = NULL;
	return node;
}

tile_t	***init_map(int weight, int height)
{
	tile_t	***tiles = malloc(sizeof(tile_t **) * (height + 1));

	if (!tiles)
		return NULL;
	for (int i = 0; i < height; i++) {
		tiles[i] = gen_line(weight);
		if (!tiles[i])
			return NULL;
	}
	tiles[height] = NULL;
	return tiles;
}

void	free_map(tile_t ***map)
{
	for (int i = 0; map[i]; i++) {
		for (int j = 0; map[i][j]; j++) {
			free(map[i][j]->clients);
			free(map[i][j]);
		}
		free(map[i]);
		map[i] = NULL;
	}
	free(map);
	map = NULL;
}