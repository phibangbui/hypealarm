def update_visited(postlist):
	new_visited = open('visited.txt', 'w')
	for post in postlist:
		new_visited.write("%s\n" % post)



old_visited = [post.rstrip('\n') for post in open('visited.txt')]

get_posts(old_visited) 

update_visited(['things', 'morethings'])
