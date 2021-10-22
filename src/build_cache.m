% Load metadata file
% Change to rel path of wiki.mat
load('../imdb/wiki.mat');
% Extract required fields and build metadata
full_path = 'imdb/' + string(wiki.full_path)';
age = floor((now - wiki.dob')/365);
gender = wiki.gender';
metadata = [full_path age gender];
% Clean and sort metadata
metadata = metadata(~ismissing(metadata(:,3)),:);
metadata = sortrows(metadata);
% Save metadata to metadata.csv
writematrix(metadata,'cache.csv');