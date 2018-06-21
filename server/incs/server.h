/*
** EPITECH PROJECT, 2018
** Project Name
** File description:
** server
*/

#ifndef SERVER_H_
	#define SERVER_H_

	#include "parse.h"
	#include "commands.h"
	#include "map.h"
	#include <string.h>
	#include <math.h>
	#include <signal.h>

typedef struct command_s command_t;
typedef struct	tile_s tile_t;

typedef	struct client_s
{
	int	fd;
	int	food;
	int	linemate;
	int	demaumere;
	int	sibur;
	int	mendiane;
	int	phiras;
	int	thystame;
	int	level;
	int	posX;
	int	posY;
	int	id;
	int	orientation;
	char	*team;
	int	is_incanting;
	command_t	**command;
}	client_t;

typedef	struct server_s
{
	int	fd;
	int	*fds;
	int	nb_fd;
	command_t	**command;
	client_t	**clients;
	tile_t		***map;
	int	nb_client;
	t_parse	*parse;
}	server_t;

void	free_queue(command_t **queue);
int	set_socket(t_parse *parse, server_t *server);
char	*getnextline(int fd);
int	start_server(t_parse *parse, server_t *server);
int	set_accept(server_t *server);
void	read_command(int c1, server_t *server);
char	*parse_command(char *command, char c, int nb);
void	append_player(tile_t **tile, client_t *client);
int	remove_player(tile_t ***map, client_t *client);
struct timeval	*get_select_timeout(server_t *server);
void	remove_time_clients(server_t *server, double last_time);
void	manage_error(int fd, int state, int *check);
command_t	*copy_cmd(command_t *command, char *name);
command_t	**queue_init();
void		queue_append(command_t ***queue, command_t *command);
command_t	*queue_get(command_t ***queue);
command_t	*queue_pop(command_t ***queue);
int		send_connection(client_t **targets, client_t *origin);
void	check_map(tile_t *map, client_t *client);
int	look_south(server_t *server, client_t *client, int *nb);
int	look_east(server_t *server, client_t *client, int *nb);
int	look_west(server_t *server, client_t *client, int *nb);
int	map_val_pos(int map_size, int pos);
int	check_fd(t_parse *parse, server_t *server, fd_set readfds);
void	remove_client(server_t *server, int fd);

#endif /* !SERVER */
