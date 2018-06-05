/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** zappy
*/

#include "server.h"

void	read_command(int c1, server_t *server)
{
	char	*str = getnextline(c1);
	
	printf("%s\n", str);
}