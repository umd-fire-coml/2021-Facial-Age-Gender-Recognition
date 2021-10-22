% Load metadata file
load('../data/wiki.mat');
% Extract required fields and build metadata
full_path = string(wiki.full_path)';
dob = datestr('wiki.dob');
gender = wiki.gender';
metadata = [full_path dob gender];
% Clean and sort metadata
metadata = metadata(~ismissing(metadata(:,3)),:);
metadata = sortrows(metadata);
% Save metadata to metadata.csv
writematrix(metadata,'metadata.csv')
