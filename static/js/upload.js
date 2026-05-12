/**
 * upload.js — Handles drag-and-drop, file preview, form loading state,
 *              and the animated SVG score ring on the results page.
 */

document.addEventListener('DOMContentLoaded', () => {

    // ── Drop Zone ────────────────────────────────────────────────────────
    const dropZone   = document.getElementById('drop-zone');
    const fileInput  = document.getElementById('resume-input');
    const preview    = document.getElementById('file-preview');
    const previewName = document.getElementById('file-preview-name');
    const removeBtn  = document.getElementById('file-remove-btn');

    if (dropZone && fileInput) {

        // Click anywhere on the zone to open the file picker
        dropZone.addEventListener('click', () => fileInput.click());

        // Drag events
        ['dragenter', 'dragover'].forEach(evt =>
            dropZone.addEventListener(evt, e => {
                e.preventDefault();
                dropZone.classList.add('drag-over');
            })
        );
        ['dragleave', 'dragend', 'drop'].forEach(evt =>
            dropZone.addEventListener(evt, () => dropZone.classList.remove('drag-over'))
        );

        dropZone.addEventListener('drop', e => {
            e.preventDefault();
            const files = e.dataTransfer.files;
            if (files.length) {
                fileInput.files = files;
                showPreview(files[0]);
            }
        });

        fileInput.addEventListener('change', () => {
            if (fileInput.files.length) showPreview(fileInput.files[0]);
        });

        if (removeBtn) {
            removeBtn.addEventListener('click', e => {
                e.stopPropagation();
                fileInput.value = '';
                preview.classList.add('hidden');
                dropZone.classList.remove('hidden');
            });
        }
    }

    function showPreview(file) {
        if (!preview || !previewName) return;
        previewName.textContent = file.name;
        preview.classList.remove('hidden');
        // Optionally hide the drop zone visual (keep it visible so user can swap)
    }

    // ── Form Loading State ────────────────────────────────────────────────
    const form      = document.getElementById('analyze-form');
    const submitBtn = document.getElementById('submit-btn');

    if (form && submitBtn) {
        form.addEventListener('submit', () => {
            const defaultState  = submitBtn.querySelector('.btn-default-state');
            const loadingState  = submitBtn.querySelector('.btn-loading-state');
            if (defaultState) defaultState.classList.add('hidden');
            if (loadingState) loadingState.classList.remove('hidden');
            submitBtn.disabled = true;
        });
    }

    // ── Animated Score Ring (results page) ───────────────────────────────
    const ringFill   = document.getElementById('score-ring-fill');
    const scoreNum   = document.getElementById('score-number');

    if (ringFill && scoreNum) {
        const score       = parseFloat(ringFill.dataset.score) || 0;
        const circumference = 427.26; // 2π × 68

        // Inject SVG gradient definition into the SVG element
        const svg = ringFill.closest('svg');
        if (svg) {
            const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
            defs.innerHTML = `
                <linearGradient id="score-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%"   stop-color="#6366f1"/>
                    <stop offset="100%" stop-color="#22d3ee"/>
                </linearGradient>`;
            svg.prepend(defs);
        }

        // Animate ring fill
        requestAnimationFrame(() => {
            const offset = circumference - (score / 100) * circumference;
            ringFill.style.strokeDashoffset = offset;
        });

        // Count-up number animation
        const duration = 1400;
        const start    = performance.now();
        function countUp(now) {
            const elapsed  = Math.min(now - start, duration);
            const progress = elapsed / duration;
            // Ease-out cubic
            const eased    = 1 - Math.pow(1 - progress, 3);
            scoreNum.textContent = Math.round(eased * score);
            if (elapsed < duration) requestAnimationFrame(countUp);
        }
        requestAnimationFrame(countUp);
    }

});
