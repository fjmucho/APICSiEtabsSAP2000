def get_story_data(smodel=None):
    """
    returns:
    story_data (list). The is a nested list with each element consists of
    [story_nm,story_ele,story_hgt,is_master_story,similar_to,splice_above,splice_height]
    """
    #Get the data using API
    #Separate the data to lists
    # story_in = smodel.Story.GetStories()
    # print(story_in) # tupla ...
    # print(story_in[8]) # no puedo optener el color por alguna razon me devuelve 0
    # print(len(story_in)) # ademas siempre devuelve 9, porque solo contamos con 9 campos en etabs
    nos_stories = 0 #NumberStories
    story_nms = [] #StoryNames
    story_eles = [] #StoryElevations
    story_hgts = [] #StoryHeights
    is_master_story = [] #IsMasterStory
    similar_to_story = [] #SimilarToStory
    splice_above = [] #SpliceAbove
    splice_height=[] #SpliceHeight
    color=0.0
    (nos_stories, story_nms, story_eles, story_hgts, is_master_story, similar_to_story, \
      splice_above, splice_height,color) = smodel.Story.GetStories(
        nos_stories, story_nms, story_eles, story_hgts, 
        is_master_story, similar_to_story, splice_above, splice_height)

    #Combine data into one list called story_data
    story_data=[];
    for i in range(len(story_nms)):
        j=-1-i;
        story_data.append([story_nms[j],
                           round(story_hgts[j],3),
                           round(story_eles[j],3),
                           is_master_story[j],
                           similar_to_story[j],
                           splice_above[j],
                           splice_height[j]]);
    return story_data;

def set_story_data(smodel=None):
    pass