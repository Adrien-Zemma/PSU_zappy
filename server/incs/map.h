/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Map H file
*/

#ifndef MAP_H_
	#define MAP_H_

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "server.h"

#define ADD_MINERAL(a, b)  (rand() % (b - a) + a)

typedef struct client_s client_t;

typedef struct	tile_s {
	int		minPlayers;
	int		linemate;
	int		deraumere;
	int		sibur;
	int		mendiane;
	int		phiras;
	int		thystam;
	int		food;
	client_t	**clients;
}			tile_t;

tile_t	***init_map(int weight, int height);
void	free_map(tile_t ***map);

extern const tile_t level_requirement[6];

#endif /* !MAP_H_ */
