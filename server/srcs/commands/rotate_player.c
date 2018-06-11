/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	forwardY(server_t *server, client_t *client)
{
	if (client->orientation == 3){
		if (client->posY == server->parse->height - 1)
			client->posY = 0;
		else
			client->posY++;
	}
	if (client->orientation == 4){
		if (client->posX == 0)
			client->posX = server->parse->width - 1;
		else
			client->posX++;
	}		
}

void	forward(server_t *server, client_t *client, char *str)
{
	str = str;
	if (client->orientation == 1){
		if (client->posY == 0)
			client->posY = server->parse->height - 1;
		else
			client->posY--;
	}
	if (client->orientation == 2){
		if (client->posX == server->parse->width -1)
			client->posX = 0;
		else
			client->posX++;
	}
	forwardY(server, client);
}

void	right(server_t *server, client_t *client, char *str)
{
	
}