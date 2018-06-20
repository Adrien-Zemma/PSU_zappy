/*
** EPITECH PROJECT, 2018
** Zappy
** File description:
** Commands C file
*/

#include "commands.h"
#include "parse.h"

command_t	**init_commands(t_parse *parse)
{
	const int	i = 21;
	command_t	**node = malloc(sizeof(command_t *) * (i + 1));

	if (!node)
		return NULL;
	node[0] = append_command("msz", map_size);
	node[1] = append_command("tna", names_team);
	node[2] = append_command("mct", map_content);
	node[3] = append_command("bct", tile_content);
	node[4] = append_command("plv #", player_level);
	node[5] = append_command("pin #", player_inventory);
	node[6] = append_command("ppo #", player_position);
	node[7] = append_command("Forward", forward);
	node[8] = append_command("Right", right);
	node[9] = append_command("Left", left);
	node[10] = append_command("inventory", inventory);
	node[11] = append_command("Look", look);
	node[12] = append_command("Broadcast", broadcast);
	node[13] = append_command("Take", take_object);
	node[14] = append_command("Connect_nbr", nb_connect);
	node[15] = append_command("sgt", sgt);
	node[16] = append_command("sst", sst);
	node[17] = append_command("Set", set_object);
	node[18] = append_command("gnp", get_number_player);
	node[19] = append_command("gnp", get_number_player);
	node[20] = append_command("ppo", get_player_pos);
	node[i] = NULL;
	return node;
}

command_t	*append_command(char *name, int (*ptrFnct)(server_t *, client_t *, char *), double time)
{
	command_t	*node = malloc(sizeof(command_t));

	if (!node)
		return NULL;
	node->time = time;
	node->name = name;
	node->ptrFnct = ptrFnct;
	return node;
}
