


function compressImage(tag, targetWidth = 800, targetHeight = 800, quality = 0.7) {
    

    const $imageInput = tag;
    const $submitRow = $('.submit-row');
    const $saveButtons = $('input[name="_save"], input[name="_continue"], input[name="_addanother"]');

    const compressHtml = `<div id='compressing-label'></div><div id='progressBarContainer'></div>`;
    $submitRow.before(compressHtml);

    const $progressBarContainer = $('#progressBarContainer');
    const $compressingLabel = $('#compressing-label'); 

    $imageInput.on('change', function(event) {
        const files = event.target.files;

        

        if (files.length > 0) {
            // Disable save buttons
            $saveButtons.prop('disabled', true);   
            $compressingLabel.show(); // Show compressing label
            $progressBarContainer.show(); // Show the progress bar 
        
            let totalFiles = files.length; 
            let processedFiles = 0;
        
            // Create progress bar elements
            const $progressBar = $('<div></div>').css({
                width: '100%',
                backgroundColor: '#f3f3f3',
                borderRadius: '5px',
                overflow: 'hidden'
            });

            const $progress = $('<div></div>').css({
                width: '0%',
                height: '20px',
                backgroundColor: '#4caf50'
            });

            $progressBar.append($progress);
            $progressBarContainer.append($progressBar);

            function processFile(file) {
                const reader = new FileReader();

                reader.onloadstart = function() {
                    $progress.css('width', '0%'); // Reset progress bar
                };

                reader.onprogress = function(e) {
                    if (e.lengthComputable) {
                        const percentLoaded = Math.round((e.loaded / e.total) * 100);
                        $progress.css('width', percentLoaded + '%');
                    }
                };

                reader.onloadend = function() {
                    $progress.css('width', '100%');
                };

                reader.onload = function(e) {
                    const img = new Image();
                    img.onload = function() {
                        const canvas = document.createElement('canvas');
                        const ctx = canvas.getContext('2d');

                        const maxWidth = targetWidth;
                        const maxHeight = targetHeight;
                        let width = img.width;
                        let height = img.height;

                        if (width > height) {
                            if (width > maxWidth) {
                                height = Math.round(height *= maxWidth / width);
                                width = maxWidth;
                            }
                        } else {
                            if (height > maxHeight) {
                                width = Math.round(width *= maxHeight / height);
                                height = maxHeight;
                            }
                        }

                        canvas.width = width;
                        canvas.height = height;

                        ctx.drawImage(img, 0, 0, width, height);

                        // Show a pseudo progress during the compression phase
                        let pseudoProgress = 0;
                        const pseudoProgressInterval = setInterval(() => {
                            if (pseudoProgress < 80) {
                                pseudoProgress += 5;
                                $progress.css('width', pseudoProgress + '%');
                            } else {
                                clearInterval(pseudoProgressInterval);
                            }
                        }, 100);

                        canvas.toBlob(function(blob) {
                            clearInterval(pseudoProgressInterval);
                            $progress.css('width', '100%');

                            const dataTransfer = new DataTransfer();
                            const fileName = file.name.replace(/\.[^/.]+$/, "") + ".jpg";
                            const newFile = new File([blob], fileName, { type: 'image/jpeg' });

                            // Replace the current file in the input with the compressed file
                            const newFiles = Array.from(event.target.files);
                            const fileIndex = newFiles.findIndex(f => f.name === file.name);
                            if (fileIndex !== -1) {
                                newFiles[fileIndex] = newFile;
                            }
                            const updatedDataTransfer = new DataTransfer();
                            newFiles.forEach(f => updatedDataTransfer.items.add(f));
                            event.target.files = updatedDataTransfer.files;

                            processedFiles++;
                            if (processedFiles === totalFiles) {
                                // Enable save buttons and hide the label after a short delay
                                setTimeout(() => {
                                    $saveButtons.prop('disabled', false);
                                    $compressingLabel.hide();
                                    $progressBarContainer.hide();
                                    $progressBar.remove();
                                }, 100);
                            }
                        }, 'image/jpeg', quality); // Adjust the quality as needed
                        console.log('width ', targetWidth, ' height ', targetHeight, ' quality ', quality);

                    };
                    img.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }

            // Process each file
            $.each(files, function(_, file) {
                processFile(file);
            });
        }

    });

}
