% Load metadata file
% Use own path
load('../wiki.mat');
% Extract required fields and build metadata
full_path = 'imdb/' + string(wiki.full_path)';
age = wiki.photo_taken' - floor((wiki.dob')/365);
gender = wiki.gender';
metadata = [full_path age gender];
% Clean and sort metadata
metadata = metadata(~ismissing(metadata(:,3)),:);
metadata = metadata(str2double(metadata(:,2))>=0,:);
metadata = metadata(str2double(metadata(:,2))<=100,:);
metadata = sortrows(metadata);
% Save metadata to metadata.csv
writematrix(metadata,'metadata.csv');