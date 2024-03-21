# BlinkBox DRF API
Welcome to the BlinkBox DRF API documentation. BlinkBox is a social media platform focused on sharing images and connecting with friends. This API provides backend support for managing user profiles, posts, likes, friends, and saved posts.

## Models Overview
### Profile
The Profile model stores additional information about users, including their profile picture, bio, birth date, and the date they joined the platform.

Fields:

owner: One-to-one relationship with the User model (linked by username). Represents the user associated with the profile.
profile_picture: ImageField for storing the user's profile picture.
bio: TextField for the user's biography.
birth_date: DateField for the user's birth date.
created_at: DateTimeField indicating the creation date of the profile.


### Posts
The Posts model represents the posts shared by users on the BlinkBox platform. Each post contains content, a title, optional location, and an image.

Fields:

owner: ForeignKey to the User model, representing the user who created the post.
created_at: DateTimeField indicating when the post was created.
content: TextField containing the content of the post.
title: CharField for the title of the post.
location: CharField for the location associated with the post.
image: ImageField for uploading and storing the image associated with the post.


### Likes
The Likes model tracks users' reactions to posts, allowing them to express like, love, or laugh sentiments.

Fields:

owner: ForeignKey to the User model, representing the user who reacted to the post.
post: ForeignKey to the Post model, indicating the post that was reacted to.
created_at: DateTimeField indicating when the reaction was made.
reaction_type: CharField with choices for the type of reaction (like, love, or laugh).


### Friends
The Friends model manages friend connections between users, including friend requests and accepted friendships.

Fields:

sender: ForeignKey to the User model, representing the user who sent the friend request.
receiver: ForeignKey to the User model, representing the user who received the friend request.
accepted: BooleanField indicating whether the friend request has been accepted.
created_at: DateTimeField indicating when the friend request was sent.


### SavedPost
The SavedPost model allows users to save posts to their profile for later viewing.

Fields:

user: ForeignKey to the User model, representing the user who saved the post.
post: ForeignKey to the Post model, indicating the post that was saved.
saved_at: DateTimeField indicating when the post was saved.
is_saved: BooleanField indicating whether the post is currently saved.


## Endpoints
The BlinkBox DRF API provides endpoints for performing CRUD operations on the models described above. These endpoints enable users to:

Create, retrieve, update, and delete profiles, posts, likes, friends, and saved posts.
Send and accept friend requests.
React to posts with likes, loves, or laughs.
Save and unsave posts to their profile.

## Testing

## Fixed Bugs

## Deployment

## Credits
