/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** server
*/

#ifndef SERVER_H_
	#define SERVER_H_

#include "parse.h"

typedef	struct server_s
{
	int	fd;
	int	*fds;
	int	nb_fd;
}	server_t;

int	set_socket(t_parse *parse, server_t *server);
char	*getnextline(int fd);
int	start_server(t_parse *parse, server_t *server);

#endif /* SERVER */

