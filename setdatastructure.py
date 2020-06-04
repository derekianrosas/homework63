#set is kind of a merge of list, a set requires that all the elements are unique, does nout allow for duplicates
#tags = {
#	'python',
#    'tutorials'
#	'coding'
#}

#tags_two = {
#	'ruby',
#	'coding',
#	'tutorials',
#	'development'
#}
#print(tags)
#set does not support indexing, not used for indexing set is all about uniqueness
#Nope
#print(tags[0])
#collection of different elements that need to be unique
#query_one = 'python' in tags
#query_two = 'ruby' in tags
#print(query_one)
#print(query_two)
tags_one = {
	'python',
	'coding',
	'tutorials',
	'coding'
}

tags_two = {
	'ruby',
	'coding',
	'tutorials',
	'development'
}

#merged tags
#merged_tags = tags | tags_two
#print(merged_tags)

#tags in tags_one but not in tags_two, a prpogram that needs to function like a venn diagram a set allows you to cresate a sort of venn diagram
#exclusive_to_tag_one = tags - tags_two
#print(exclusive_to_tag_one)

# tags found in both tags and tags_two
universal_tags = tags_one & tags_two
print(universal_tags)